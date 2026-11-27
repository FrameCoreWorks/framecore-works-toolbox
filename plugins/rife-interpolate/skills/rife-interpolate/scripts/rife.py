#!/usr/bin/env python3
"""FrameCore Works launcher for RIFE frame interpolation (rife-ncnn-vulkan).

Our own code. It downloads the pinned TNTwise/rife-ncnn-vulkan release only
after the user's yes, checks its SHA-256, keeps the program and the chosen
models outside the project, and runs it on a video through ffmpeg.

Commands (each prints one JSON object):
  status                       what is installed and what this host can use
  plan [--models a,b]          what install would download and write
  install --yes [--models a,b] download, verify and unpack the pinned release
  run INPUT OUTPUT [options]   interpolate a video (see run --help)
  sheet RESULT OUTPUT.png      three consecutive output frames for the QA look

Standard library only; needs ffmpeg and ffprobe on PATH for run and sheet. On Linux
it needs a Vulkan driver; without a GPU, Mesa's llvmpipe (mesa-vulkan-drivers,
libvulkan1), installed only after the user's yes.
"""

import argparse
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from fractions import Fraction
from pathlib import Path

UPSTREAM = "https://github.com/TNTwise/rife-ncnn-vulkan"
RELEASE = "20250112"
COMMIT = "5eea93c6e7079dda69d7a0ce9c1106ff5e641143"
# Release assets reviewed on 2026-11-27 (reviews/rife-interpolate.md).
ASSETS = {
    "macos": {"file": "macos.zip", "bytes": 830643776,
              "sha256": "543bf845a6160d8ad29a10c2b7a0713e78781dc2505c62185f7d14c3265bb4c0"},
    "linux-x86_64": {"file": "ubuntu.zip", "bytes": 825856265,
                     "sha256": "a4166da15a9839350a3695c35d9e19288c5c48c0fc9afc5aacb766d3d7f8ab62"},
}
DEFAULT_MODELS = ("rife-v4.26",)
# Linux without a GPU needs a Vulkan driver: Mesa's llvmpipe runs Vulkan on the CPU.
# The release's own CPU path (-g -1) wrote garbage in-between frames in our test
# (2026-11-27, Linux x86_64, rife-v4.26 and rife-v4.6), so it is never used.
LINUX_VULKAN = ("mesa-vulkan-drivers", "libvulkan1")
ICD_DIRS = ("/usr/share/vulkan/icd.d", "/etc/vulkan/icd.d")
BINARY = "rife-ncnn-vulkan"


def host_key():
    system, machine = platform.system(), platform.machine().lower()
    if system == "Darwin":
        return "macos"  # universal binary: Apple Silicon and Intel
    if system == "Linux" and machine in ("x86_64", "amd64"):
        return "linux-x86_64"
    return None


def home():
    base = os.environ.get("FRAMECORE_RIFE_HOME")
    root = Path(base).expanduser() if base else Path.home() / ".cache" / "framecore" / "rife"
    return root / RELEASE


def receipt_path():
    return home() / "installation.json"


def read_receipt():
    try:
        return json.loads(receipt_path().read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def emit(data, code=0):
    print(json.dumps(data, indent=2, ensure_ascii=False))
    return code


def parse_models(text):
    models = tuple(m.strip() for m in (text or "").split(",") if m.strip()) or DEFAULT_MODELS
    for model in models:
        if not model.startswith("rife") or "/" in model or ".." in model:
            raise SystemExit(emit({"status": "error", "reason": f"invalid model name {model!r}"}, 2))
    return models


def cmd_status(_args):
    receipt = read_receipt()
    return emit({
        "status": "installed" if receipt else "not_installed",
        "host": host_key() or f"unsupported ({platform.system()} {platform.machine()})",
        "release": RELEASE,
        "home": str(home()),
        "models": receipt.get("models", []) if receipt else [],
        "ffmpeg": bool(shutil.which("ffmpeg") and shutil.which("ffprobe")),
        "vulkan": "ready" if vulkan_ready() else
                  "missing: ask the user, then install " + " ".join(LINUX_VULKAN) + " (apt-get)",
    })


def cmd_plan(args):
    key = host_key()
    if key is None:
        return emit({"status": "unsupported_host",
                     "reason": f"no reviewed release asset for {platform.system()} {platform.machine()}"}, 3)
    asset = ASSETS[key]
    return emit({
        "status": "plan",
        "download": f"{UPSTREAM}/releases/download/{RELEASE}/{asset['file']}",
        "download_mb": round(asset["bytes"] / 1e6),
        "sha256": asset["sha256"],
        "writes": str(home()),
        "keeps": [BINARY, "LICENSE", *parse_models(args.models)],
        "kept_mb_approx": 12 * len(parse_models(args.models)) + 30,
        "note": "The archive is deleted after unpacking. Nothing is written into the project.",
        "needs": "the user's yes, then: install --yes",
    })


def cmd_install(args):
    if not args.yes:
        return emit({"status": "needs_consent", "reason": "run plan, ask the user, then install --yes"}, 4)
    key = host_key()
    if key is None:
        return cmd_plan(args)
    models = parse_models(args.models)
    asset, target = ASSETS[key], home()
    receipt = read_receipt()
    if receipt and set(models) <= set(receipt.get("models", [])):
        return emit({"status": "already_installed", "home": str(target), "models": receipt["models"]})
    target.mkdir(parents=True, exist_ok=True)
    url = f"{UPSTREAM}/releases/download/{RELEASE}/{asset['file']}"
    with tempfile.TemporaryDirectory(dir=target) as tmp:
        archive = Path(tmp) / asset["file"]
        digest = hashlib.sha256()
        with urllib.request.urlopen(url, timeout=120) as response, archive.open("wb") as out:
            while True:
                chunk = response.read(1 << 20)
                if not chunk:
                    break
                digest.update(chunk)
                out.write(chunk)
        if digest.hexdigest() != asset["sha256"]:
            return emit({"status": "error", "reason": "SHA-256 mismatch; nothing was installed",
                         "expected": asset["sha256"], "got": digest.hexdigest()}, 5)
        wanted = {BINARY, "LICENSE", *models}
        found = set()
        with zipfile.ZipFile(archive) as zipped:
            for info in zipped.infolist():
                parts = Path(info.filename).parts
                if len(parts) < 2 or parts[1] not in wanted or info.is_dir() or ".." in parts:
                    continue
                destination = target.joinpath(*parts[1:])
                destination.parent.mkdir(parents=True, exist_ok=True)
                with zipped.open(info) as source, destination.open("wb") as out:
                    shutil.copyfileobj(source, out)
                found.add(parts[1])
    missing = sorted(wanted - found)
    if missing:
        return emit({"status": "error", "reason": "not in the release", "missing": missing}, 6)
    (target / BINARY).chmod(0o755)
    all_models = sorted(set(models) | set((receipt or {}).get("models", [])))
    data = {"release": RELEASE, "commit": COMMIT, "asset": asset["file"],
            "sha256": asset["sha256"], "models": all_models}
    receipt_path().write_text(json.dumps(data, indent=2), encoding="utf-8")
    return emit({"status": "installed", "home": str(target), **data})


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=r_frame_rate,width,height", "-show_entries", "format=duration",
         "-of", "json", str(path)], check=True, capture_output=True, text=True).stdout
    data = json.loads(out)
    stream = data["streams"][0]
    has_audio = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index",
         "-of", "csv=p=0", str(path)], capture_output=True, text=True).stdout.strip() != ""
    return Fraction(stream["r_frame_rate"]), stream["width"], stream["height"], has_audio


def target_frames(count, src_fps, fps=None, factor=None):
    """Frames RIFE must produce so that the output keeps the source duration."""
    if fps:
        return max(count, round(count * Fraction(str(fps)) / src_fps))
    return count * int(factor or 2)


def vulkan_ready():
    if platform.system() != "Linux":
        return True  # macOS: MoltenVK is linked into the binary
    return any(Path(p).is_dir() and any(Path(p).glob("*.json")) for p in ICD_DIRS)


def device_args():
    # Linux is usually a cloud container on llvmpipe: more processing threads help there.
    return ["-j", "1:4:2"] if platform.system() == "Linux" else []


def ratio_needs_v4(src_fps, fps=None):
    """Only RIFE v4 models make frames at any time step; older ones only halve."""
    if not fps:
        return False
    ratio = Fraction(str(fps)) / src_fps
    return ratio.denominator != 1 or ratio.numerator & (ratio.numerator - 1) != 0


def cmd_run(args):
    receipt = read_receipt()
    if not receipt:
        return emit({"status": "not_installed", "next": "plan, ask the user, install --yes"}, 7)
    if args.model not in receipt["models"]:
        return emit({"status": "model_missing", "model": args.model,
                     "next": f"install --yes --models {args.model}"}, 7)
    if not (shutil.which("ffmpeg") and shutil.which("ffprobe")):
        return emit({"status": "error", "reason": "ffmpeg and ffprobe are needed"}, 8)
    if not vulkan_ready():
        return emit({"status": "needs_vulkan_driver", "packages": list(LINUX_VULKAN),
                     "next": "ask the user, then: apt-get install -y " + " ".join(LINUX_VULKAN)}, 9)
    src, dst = Path(args.input).resolve(), Path(args.output).resolve()
    src_fps, width, height, has_audio = probe(src)
    if ratio_needs_v4(src_fps, args.fps) and not args.model.startswith("rife-v4"):
        return emit({"status": "error", "reason": f"{float(src_fps):g} to {args.fps:g} fps needs a rife-v4 model"}, 2)
    work = Path(tempfile.mkdtemp(prefix="rife-", dir=args.work_dir))
    frames_in, frames_out = work / "in", work / "out"
    frames_in.mkdir()
    frames_out.mkdir()
    extract = ["ffmpeg", "-nostdin", "-v", "error", "-i", str(src), "-vsync", "0"]
    if args.max_height and height > args.max_height:
        extract += ["-vf", f"scale=-2:{args.max_height}:flags=lanczos"]
        width, height = round(width * args.max_height / height), args.max_height
    subprocess.run(extract + [str(frames_in / "%08d.png")], check=True)
    count = len(list(frames_in.glob("*.png")))
    total = target_frames(count, src_fps, args.fps, args.factor)
    command = [str(home() / BINARY), "-i", str(frames_in), "-o", str(frames_out),
               "-m", str(home() / args.model), "-n", str(total), *device_args()]
    if args.uhd or max(width, height) > 2000:
        command.append("-u")
    subprocess.run(command, check=True, capture_output=True)
    made = len(list(frames_out.glob("*.png")))
    if args.slowmo:
        out_fps = src_fps  # same rate, more frames: slow motion, original sound dropped
    else:
        out_fps = Fraction(str(args.fps)) if args.fps else src_fps * int(args.factor or 2)
    encode = ["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(out_fps),
              "-i", str(frames_out / "%08d.png")]
    if has_audio and not args.slowmo:
        encode += ["-i", str(src), "-map", "0:v", "-map", "1:a", "-c:a", "copy", "-shortest"]
    encode += ["-frames:v", str(total), "-c:v", "libx264", "-crf", str(args.crf), "-preset", "slow",
               "-pix_fmt", "yuv420p", str(dst)]
    subprocess.run(encode, check=True)
    if not args.keep_frames:
        shutil.rmtree(work, ignore_errors=True)
    return emit({"status": "done", "output": str(dst), "model": args.model,
                 "source_fps": float(src_fps), "output_fps": float(out_fps),
                 "frames_in": count, "frames_out": made, "slowmo": bool(args.slowmo),
                 "audio": "dropped (slow motion)" if args.slowmo and has_audio else
                          ("copied" if has_audio else "none"),
                 "frames_kept": str(work) if args.keep_frames else None,
                 "next": "check frames on fast motion, text and edges (sheet RESULT OUT.png --at SECONDS)"})


def cmd_sheet(args):
    """Three consecutive frames of a 2x result: source, interpolated, source."""
    result, out = Path(args.result), Path(args.output)
    fps = probe(result)[0]
    first = int(round(args.at * fps)) // 2 * 2  # even index = a source frame in a 2x run
    vf = (f"select='between(n\\,{first}\\,{first + 2})',setpts=N/TB,"
          "scale='min(640,iw)':-2,tile=3x1:padding=8:color=white")
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(result), "-vf", vf,
                    "-frames:v", "1", str(out)], check=True)
    return emit({"status": "done", "sheet": str(out), "frames": [first, first + 1, first + 2],
                 "read": "a 2x run: left and right are source frames, the middle one is new; other rates: three consecutive output frames"})


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status").set_defaults(func=cmd_status)
    plan = sub.add_parser("plan")
    plan.add_argument("--models")
    plan.set_defaults(func=cmd_plan)
    install = sub.add_parser("install")
    install.add_argument("--yes", action="store_true")
    install.add_argument("--models")
    install.set_defaults(func=cmd_install)
    run = sub.add_parser("run")
    run.add_argument("input")
    run.add_argument("output")
    rate = run.add_mutually_exclusive_group()
    rate.add_argument("--factor", type=int, choices=(2, 3, 4, 8))
    rate.add_argument("--fps", type=float)
    run.add_argument("--slowmo", action="store_true", help="keep the frame rate: the clip plays slower")
    run.add_argument("--model", default=DEFAULT_MODELS[0])
    run.add_argument("--max-height", type=int, help="scale down first (cloud previews, e.g. 960)")
    run.add_argument("--uhd", action="store_true")
    run.add_argument("--crf", type=int, default=16)
    run.add_argument("--keep-frames", action="store_true")
    run.add_argument("--work-dir")
    run.set_defaults(func=cmd_run)
    sheet = sub.add_parser("sheet")
    sheet.add_argument("result", help="a run output made with --factor 2")
    sheet.add_argument("output")
    sheet.add_argument("--at", type=float, default=0.5)
    sheet.set_defaults(func=cmd_sheet)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

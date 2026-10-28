#!/usr/bin/env python3
"""Compatibility entry point; the plugin-root launcher owns the pinned Earshot runtime."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    launcher = Path(__file__).resolve().parents[3] / "scripts" / "runtime.py"
    runpy.run_path(str(launcher), run_name="__main__")

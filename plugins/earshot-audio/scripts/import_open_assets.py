#!/usr/bin/env python3
"""Compatibility command for existing source sidecars; no plugin dependency."""
import runpy
from pathlib import Path

if __name__ == '__main__':
    runpy.run_path(str(Path(__file__).with_name('import_source_record.py')), run_name='__main__')

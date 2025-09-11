#!/usr/bin/env python3
import os, sys, zipfile
from datetime import datetime

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: backup_zip.py <folder>"); sys.exit(1)
    folder = sys.argv[1]
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    out = f"backup_{ts}.zip"
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for r, _, files in os.walk(folder):
            for name in files:
                p = os.path.join(r, name)
                z.write(p, os.path.relpath(p, folder))
    print("Wrote", out)

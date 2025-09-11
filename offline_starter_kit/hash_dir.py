#!/usr/bin/env python3
import hashlib, os, sys

def sha256_file(path, chunk=65536):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            b = f.read(chunk)
            if not b: break
            h.update(b)
    return h.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: hash_dir.py <dir>"); sys.exit(1)
    root = sys.argv[1]
    for r, _, files in os.walk(root):
        for name in files:
            p = os.path.join(r, name)
            try:
                print(sha256_file(p), p)
            except Exception as e:
                print("ERROR:", p, e)

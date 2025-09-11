#!/usr/bin/env python3
import re, sys
from collections import Counter

PATTERN = re.compile(r"(?P<ip>\d+\.\d+\.\d+\.\d+).+?(?P<ts>\d{2}:\d{2}:\d{2})")

def parse(path):
    ips = Counter()
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            m = PATTERN.search(line)
            if m:
                ips[m.group('ip')] += 1
    return ips

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: regex_log_parser.py <logfile>"); sys.exit(1)
    counts = parse(sys.argv[1])
    for ip, c in counts.most_common():
        print(ip, c)

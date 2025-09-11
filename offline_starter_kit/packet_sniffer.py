#!/usr/bin/env python3
# Requires scapy: pip install scapy
from scapy.all import sniff
from collections import Counter

counts = Counter()

def handler(pkt):
    proto = pkt.payload.name if hasattr(pkt, 'payload') else 'UNK'
    counts[proto] += 1

if __name__ == "__main__":
    print("Sniffing 100 packets on default interface (Ctrl+C to stop)...")
    sniff(count=100, prn=handler, store=False)
    print("Summary by higher-level payload name:")
    for k, v in counts.most_common():
        print(f"{k}: {v}")

#!/usr/bin/env python3
import socket, argparse, sys
from datetime import datetime

def scan(host, start_port, end_port, timeout=0.5):
    print(f"Scanning {host} from {start_port} to {end_port}...")
    for port in range(start_port, end_port+1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                if s.connect_ex((host, port)) == 0:
                    print(f"OPEN: {port}")
        except KeyboardInterrupt:
            print("\nInterrupted"); sys.exit(1)
        except Exception:
            pass

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Simple TCP port scanner (lab use only)")
    ap.add_argument("--host", required=True)
    ap.add_argument("--start-port", type=int, default=1)
    ap.add_argument("--end-port", type=int, default=1024)
    args = ap.parse_args()
    t0 = datetime.now()
    scan(args.host, args.start_port, args.end_port)
    print("Done in", datetime.now()-t0)

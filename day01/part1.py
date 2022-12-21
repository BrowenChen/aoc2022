from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def result(s: str) -> int:
    return max(sum(int(line) for line in elf.splitlines()) for elf in s.split('\n\n'))

def main() -> int:
    with open(INPUT_TXT) as f:
        print(result(f.read()))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

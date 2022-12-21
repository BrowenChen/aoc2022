from __future__ import annotations

import argparse
from typing import List
import os.path
import heapq

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def execute(s: str, n: int) -> int:
    elf_calories: List = []
    for elf in s.split('\n\n'):
        heapq.heappush(elf_calories, sum(int(line) for line in elf.splitlines()))
    return sum(heapq.nlargest(n, elf_calories))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', help='Number of elves')
    args = parser.parse_args()
    with open(INPUT_TXT) as f:
        print(execute(f.read(), int(args.number)))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

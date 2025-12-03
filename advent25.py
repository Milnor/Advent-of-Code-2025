"""Advent of Code 2025."""

import argparse
from pathlib import Path

from src.advent25.challenge import DailyChallenge
from src.advent25.day01 import Day01
from src.advent25.day02 import Day02
from src.advent25.day03 import Day03

RES = "\033[00m"    # RESET
BLD = "\033[1m"     # BOLD
UND = "\033[4m"     # UNDERLINE
STK = "\033[9m"     # STRIKETHROUGH
GRA = "\033[30m"    # GRAY
RED = "\033[31m"
GRE = "\033[32m"    # GREEN
YEL = "\033[33m"
BLU = "\033[34m"
MAG = "\033[35m"
CYN = "\033[36m"
WHI = "\033[37m"

STAR = "⭐"
TREE = "🎄"
SANTA = "🎅 🎄 🎁 ✨"
GIFT = "🎁"

def main(args: argparse.Namespace):

    if args.day is not None:
        # Actually, I ought to implement that factory sooner rather than later.
        day3: DailyChallenge = Day03(
            Path("data/day03.txt"),
            Path("data/day03.txt"),
            Path("data/sample/day03.txt")
        )
        print(f"{day3.sample1=}")
        print(f"{day3.sample2=}")
        exit(1)

    day1: DailyChallenge = Day01(
        Path("data/day01.txt"),
        Path("data/day01.txt"),
        Path("data/sample/day01.txt")
    )

    day2: DailyChallenge = Day02(
        Path("data/day02.txt"),
        Path("data/day02.txt"),
        Path("data/sample/day02.txt")
    )

    day3: DailyChallenge = Day03(
        Path("data/day03.txt"),
        Path("data/day03.txt"),
        Path("data/sample/day03.txt")
    )

    for day in [day1, day2, day3]:
        print(f" {RED}{day.sample1} {GRE}{day.part1} {YEL}{day.sample2} "
              f"{GRE}{day.part2}{RES}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    description='Advent of Code 2025',
                    epilog='Merry Christmas, ya filthy animal!')
    parser.add_argument('-d', '--day', type=int, help="limit output to a specific day's challenges")
    args = parser.parse_args()
    #print(args)
    #exit(5)
    main(args)

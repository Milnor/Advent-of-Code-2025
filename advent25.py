"""Advent of Code 2025."""

from pathlib import Path

from src.advent.challenge import DailyChallenge
from src.advent.day01 import Day01

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

def main():
    day1: DailyChallenge = Day01(
        Path("data/day01.txt"),
        Path("data/day01.txt"),
        Path("data/sample/day01.txt"))

    for day in [day1]:
        print(f" {RED}{day.sample1} {GRE}{day.part1} {YEL}{day.sample2} {GRE}{day.part2}{RES}")
    #print(day1.sample1)
    #print(day1.part1)
    #print(f"{day1.sample2=}")
    #print(day1.part2)

if __name__ == "__main__":
    main()

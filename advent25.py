"""Advent of Code 2025."""

from pathlib import Path

from src.advent.challenge import DailyChallenge
from src.advent.day01 import Day01

def main():
    day1: DailyChallenge = Day01(
        Path("data/day01.txt"),
        Path("data/day01.txt"),
        Path("data/sample/day01.txt"))
    
    print(day1.sample1)
    print(day1.part1)
    print(f"{day1.sample2=}")
    print(day1.part2)

if __name__ == "__main__":
    main()

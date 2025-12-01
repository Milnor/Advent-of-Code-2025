"""Advent of Code 2025."""

from pathlib import Path

from src.advent.challenge import DailyChallenge
from src.advent.day01 import Day01

def main():
    day1: DailyChallenge = Day01(
        Path("data/day01.txt"),
        Path("data/tbd.txt"),
        Path("data/sample/day01.txt"))
    
    print(day1.sample)
    print(day1.part1())

if __name__ == "__main__":
    main()

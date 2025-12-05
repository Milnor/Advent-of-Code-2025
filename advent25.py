"""Advent of Code 2025."""

import argparse

import src.advent25.challenge as dc
from src.advent25 import dailies

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

def main(argv: argparse.Namespace):

    daily_challenges = dc.challenge_factory(dailies)
    if argv.day is not None:
        today = daily_challenges[argv.day]

        if argv.sample == True:
            print(f"{today.sample1}, {today.sample2}")
        else:
            print(f"{today.sample1}, {today.part1}, {today.sample2}, {today.part2}")

        exit(0)

    for day in daily_challenges.values():

        if argv.sample == True:
            print(f" {RED}{day.sample1} {YEL}{day.sample2} {RES}")
        else:
            print(f" {RED}{day.sample1} {GRE}{day.part1} {YEL}{day.sample2} "
                  f"{GRE}{day.part2}{RES}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    description="Advent of Code 2025",
                    epilog="Merry Christmas, ya filthy animal!")
    parser.add_argument("-d",
                        "--day",
                        type=int,
                        help="limit output to a specific day's challenges")
    parser.add_argument("-s",
                        "--sample",
                        action="store_true",
                        help="limit output to sample data set(s)")
    args = parser.parse_args()
    main(args)

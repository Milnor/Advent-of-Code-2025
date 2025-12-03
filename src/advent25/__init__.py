"""Expose the daily challenges to main module."""

from .challenge import DailyChallenge
from .day01 import Day01
from .day02 import Day02
from .day03 import Day03

dailies = {
    1: Day01,
    2: Day02,
    3: Day03,
}

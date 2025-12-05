import unittest

import src.advent25.challenge as dc
from src.advent25 import dailies

answers: dict[int, list[int]] = {
    1: [3, 1165, 6, 6496], # sample1, part1, sample2, part2
    2: [1227775554, 17077011375, 4174379265, 36037497037],
    3: [357, 17316, 3121910778619, 171741365473332],
    4: [13, 1533, 43, 9206],
    5: [3, 733, 14]
}

daily_challenges: dict[int, dc.DailyChallenge] = dc.challenge_factory(dailies)


class TestDay01(unittest.TestCase):
    """
    --- Day 1: Secret Entrance ---
    """

    def test_day1(self):
        today = daily_challenges[1]
        self.assertEqual(today.sample1, answers[1][0])
        self.assertEqual(today.part1, answers[1][1])
        self.assertEqual(today.sample2, answers[1][2])
        self.assertEqual(today.part2, answers[1][3])


class TestDay02(unittest.TestCase):
    """
    --- Day 2: Gift Shop ---
    """

    def test_day2(self):
        today = daily_challenges[2]
        self.assertEqual(today.sample1, answers[2][0])
        self.assertEqual(today.part1, answers[2][1])
        self.assertEqual(today.sample2, answers[2][2])
        self.assertEqual(today.part2, answers[2][3])


class TestDay03(unittest.TestCase):
    """
    --- Day 3: Lobby ---
    """

    def test_part1(self):
        today = daily_challenges[3]
        self.assertEqual(today.sample1, answers[3][0])
        self.assertEqual(today.part1, answers[3][1])
        self.assertEqual(today.sample2, answers[3][2])
        self.assertEqual(today.part2, answers[3][3])


class TestDay04(unittest.TestCase):
    """
    --- Day 4: Printing Department ---
    """

    def test_part1(self):
        today = daily_challenges[4]
        self.assertEqual(today.sample1, answers[4][0])
        self.assertEqual(today.part1, answers[4][1])
        self.assertEqual(today.sample2, answers[4][2])
        self.assertEqual(today.part2, answers[4][3])


# --- Day 5: Cafeteria ---
# sample1=3
# part1=733

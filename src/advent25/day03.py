"""My solution to Day 3."""

from src.advent25 import DailyChallenge

def early_max_index(data: list[int]) -> int:
    """
    Return the index of the first occurence of the largest digit in the
     sequence.
    
    :return: Description
    :rtype: int
    """
    print(f"operating on: {data}")
    index = -1, -1  # index, value
    for i in range(len(data)):
        if data[i] > index[1]:
            index = i, data[i]

    return index[0]


def total_output_joltage(joltages: list[str]) -> int:
    """
    Calculate the maximum output joltage of each bank and return
    the sum total of all of them.
    
    :param joltages: a list of strings of numbers, e.g. ["11112485811", "443"]
    :type joltages: list[str]
    :return: sum of maximum output joltage of all entries
    :rtype: int
    """

    total: int = 0
    for bank in joltages:
        integers: list[int] = [int(digit) for digit in bank]
        first_digit_index = early_max_index(integers[:-1])
        second_digit_index = early_max_index(integers[first_digit_index + 1:]) + first_digit_index + 1
        subtotal = integers[first_digit_index] * 10 + integers[second_digit_index]
        print(f"{bank} ==> {subtotal}")
        total += subtotal

    return total

class Day03(DailyChallenge):
    """
    Day 3: Lobby
    """

    def _part1(self, use_sample_data: bool=False) -> int:
        data = self.part1_data if not use_sample_data else self.sample_data
        joltages: list[str] = self.line_to_list(data)

        # print("Quick n dirty debug:")
        # 987654321111111
        # 811111111111119
        # 234234234234278
        # 818181911112111

        return total_output_joltage(joltages)

    def _part2(self, use_sample_data: bool=False) -> int:
        data = self.part1_data if not use_sample_data else self.sample_data
        joltages: list[str] = self.line_to_list(data)

        return -1
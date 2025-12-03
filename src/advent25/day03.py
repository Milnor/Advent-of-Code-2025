"""My solution to Day 3."""

from src.advent25 import DailyChallenge

_MAX_BATTERIES = 12

def early_max_index(data: list[int]) -> int:
    """
    Return the index of the first occurence of the largest digit in the
     sequence.
    
    :return: Description
    :rtype: int
    """

    index = -1, -1  # index, value
    for i in range(len(data)):
        if data[i] > index[1]:
            index = i, data[i]

    return index[0]

def remove_smallest_from_front(data: list[int]) -> list[int]:
    """
    Remove the smallest integer (from the front of the list) until the length
     of the list is exactly _MAX_BATTERIES. --> bad logic

    Actual logic is remove the first digit n that is smaller than n + 1?
    If you can't do that, then remove the smallest digit from the front.
    """

    smaller: list[int] = data.copy()
    high_priority: list[int] = []
    victim: int = 1

    # The constraint I missed on my first attempt is that you do not remove a
    #  smaller less significant digit if it will result in a more significant
    #  digit being smaller; i.e. in the 3rd line of the sample data, you can't
    #  remove the 2 in ...278, because then you couldn't remove the 3 in 234...

    while len(smaller) != _MAX_BATTERIES:

        took_action: bool = False

        # Always expose a larger number in higher order position if possible
        for i in range(len(smaller) - 1):
            if smaller[i] < smaller[i + 1]:
                high_priority.append(i)
                break

        if len(high_priority) == 1:
            smaller.pop(high_priority.pop())
            took_action = True

        if not took_action and victim in smaller:
            smaller.remove(victim)
            took_action = True

        if took_action is False:
            victim += 1

    return smaller

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
        first_digit_idx = early_max_index(integers[:-1])
        second_digit_idx = (
            early_max_index(integers[first_digit_idx + 1:]) + \
            first_digit_idx + 1
        )
        subtotal = integers[first_digit_idx] * 10 + integers[second_digit_idx]
        total += subtotal

    return total

def total_joltage_12(joltages) -> int:
    """
    Return the total maximum output voltage with 12 batteries turned on in
     every bank.
    """

    total: int = 0
    for bank in joltages:
        integers: list[int] = [int(digit) for digit in bank]
        only_12: list[int] = remove_smallest_from_front(integers)
        only_12_strings: list[str] = [str(i) for i in only_12]
        subtotal = int("".join(only_12_strings))
        total += subtotal

    return total

class Day03(DailyChallenge):
    """
    Day 3: Lobby
    """

    def _part1(self, use_sample_data: bool=False) -> int:
        data = self.part1_data if not use_sample_data else self.sample_data
        joltages: list[str] = self.line_to_list(data)

        return total_output_joltage(joltages)

    def _part2(self, use_sample_data: bool=False) -> int:
        data = self.part1_data if not use_sample_data else self.sample_data
        joltages: list[str] = self.line_to_list(data)

        return total_joltage_12(joltages)

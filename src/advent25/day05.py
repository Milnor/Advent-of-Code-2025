"""My solution to Day 5."""

from dataclasses import dataclass

from src.advent25 import DailyChallenge

@dataclass(frozen=True)
class SafeList:
    lower: int
    upper: int


class HelloFresh:
    """Is this class name a trademark violation?"""

    def __init__(self, inputs: list[str]):
        self.ingredient_list: list[int] = []
        self.fresh_list: list[SafeList] = []
        self.safe_items: set[int] = set()
        for line in inputs:
            if len(line) < 1:
                pass
            elif "-" in line:
                numbers = line.split("-")
                lower = int(numbers[0])
                upper = int(numbers[1])
                self.fresh_list.append(SafeList(lower, upper))
            else:
                self.ingredient_list.append(int(line))

        for item in self.ingredient_list:
            for test in self.fresh_list:
                if item >= test.lower and item <= test.upper:
                    self.safe_items.add(item)
                    break

    @property
    def safe_count(self) -> int:
        """Count of safe ingredients we have on hand."""

        return len(self.safe_items)

    @property
    def total_safe_possible(self) -> int:
        """Count of all safe ingredients that exist."""

        # Correct rough draft that is not memory efficient enough for large
        #  data sets; it also got killed (presumably by OOM Killer) when I
        #  converted the ranges to generator expressions.      
        # total: set[range] = set()
        # for safe_range in self.fresh_list:
        #     new_range = range(safe_range.lower, safe_range.upper + 1)
        #     total.update(new_range)
        # return len(total)


class Day05(DailyChallenge):
    """
    Day 5: Cafeteria
    """

    def _part1(self, use_sample_data: bool=False) -> int:
        data = self.part1_data if not use_sample_data else self.sample_data
        inputs: list[str] = self.line_to_list(data)
        ingredients: HelloFresh = HelloFresh(inputs)
        return ingredients.safe_count

    def _part2(self, use_sample_data: bool=False) -> int:
        data = self.part1_data if not use_sample_data else self.sample_data
        inputs: list[str] = self.line_to_list(data)
        ingredients: HelloFresh = HelloFresh(inputs)
        return ingredients.total_safe_possible

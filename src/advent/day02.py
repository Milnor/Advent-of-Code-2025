from src.advent import DailyChallenge

class InvalidIDTotaler:
    """Process invalid IDs from ranges."""

    def __init__(self, ranges: list[str]):
        self._data: list[str] = []
        for numbers in ranges:
            #print(f"{numbers=}")
            lower, upper = numbers.split("-")
            lower = int(lower)
            upper = int(upper) + 1
            for number in range(lower, upper):
                # We could filter out numbers without an even number of digits
                #  here, but we don't know yet whether we'll need the full
                #  ranges in Part 2.
                self._data.append(str(number))

    @property
    def invalid_total(self) -> int:
        total: int = 0
        even_lengths = [number for number in self._data if len(number) % 2 == 0]
        for number in even_lengths:
            # Google's "AI Overview" gave me these 3 lines
            halfway = len(number) // 2
            first = number[:halfway]
            second = number[halfway:]
            if first == second:
                total += int(number)
        return total

class Day02(DailyChallenge):
    """
    --- Day 2: Gift Shop ---
    """

    def _part1(self, use_sample_data: bool=False) -> int:
        data = self.part1_data if not use_sample_data else self.sample_data
        ranges: list[str] = self.csv_to_list(data)
        #print(ranges)
        id_processor = InvalidIDTotaler(ranges)
        print(id_processor._data[:20])
        return id_processor.invalid_total
    
    def _part2(self, use_sample_data: bool=False) -> int:
        return 3
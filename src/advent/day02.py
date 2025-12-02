from src.advent import DailyChallenge

# Note: Not a @staticmethod of InvalidIDTotaler as per the Google Python Style
#  Guide.
def is_invalid(number: str) -> bool:
    """
    Return True if number consists of a repeating sequence of digits, otherwise
    return False.
    """

    if len(number) < 2:
        return False

    for size in range(1, len(number) // 2 + 1):
        # Adapted from list comprehension example in Google AI Overview on
        #  "python split string into n pieces".
        chunks: set[str] = {number[i:i+size] for i in range(0, len(number), size)}
        # Sets do not allow duplicates, so...
        if len(chunks) == 1:
            return True
        
    return False

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
    def invalid_total_1(self) -> int:
        """Totals all numbers consisting of a sequence that repeats once."""
        total: int = 0
        even_lengths = [number for number in self._data if len(number) % 2 == 0]
        for number in even_lengths:
            # Google's "AI Overview" gave me these 3 lines to cut str in half.
            halfway = len(number) // 2
            first = number[:halfway]
            second = number[halfway:]
            if first == second:
                total += int(number)
        return total
    
    @property
    def invalid_total_2(self) -> int:
        """Totals all numbers consisting of repeating sequences."""
        total: int = 0
        for number in self._data:
            if is_invalid(number):
                total += int(number)
        return total

class Day02(DailyChallenge):
    """
    --- Day 2: Gift Shop ---
    """

    def _part1(self, use_sample_data: bool=False) -> int:
        data = self.part1_data if not use_sample_data else self.sample_data
        ranges: list[str] = self.csv_to_list(data)
        id_processor = InvalidIDTotaler(ranges)

        return id_processor.invalid_total_1
    
    def _part2(self, use_sample_data: bool=False) -> int:
        data = self.part1_data if not use_sample_data else self.sample_data
        ranges: list[str] = self.csv_to_list(data)
        id_processor = InvalidIDTotaler(ranges)

        return id_processor.invalid_total_2

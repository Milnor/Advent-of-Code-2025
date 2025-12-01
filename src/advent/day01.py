from src.advent import DailyChallenge

class Dial:

    def __init__(self):
        self.position: int = 50

    def turn_left(self, distance: int) -> bool:
        """True if landed on 0, False otherwise."""
        self.position = (self.position - distance) % 100
        print(f"new position: ", self.position)
        return True if self.position == 0 else False

    def turn_right(self, distance: int) -> bool:
        """True if landed on 0, False otherwise."""
        self.position = (self.position + distance) % 100
        print(f"new position: ", self.position)
        return True if self.position == 0 else False

class Day01(DailyChallenge):
    """
    The first day's challenges.
    """

    def part1(self, use_sample_data: bool=False) -> int:
        data = self.part1_data if not use_sample_data else self.sample_data
        zeroes: int = 0
        dial = Dial()
        rotations: list[str] = self.line_to_list(data, False)
        for rotation in rotations:
            distance = int(rotation[1:])
            if rotation.startswith("L"):
                if dial.turn_left(distance):
                    zeroes += 1
            elif rotation.startswith("R"):
                if dial.turn_right(distance):
                    zeroes += 1
            else:
                raise ValueError(f"Expected 'L' or 'R', got {rotation[0]}")
        return zeroes

    def part2(self) -> int:
        raise NotImplementedError
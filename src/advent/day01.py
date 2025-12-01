from src.advent import DailyChallenge

class Dial:
    """Dial that returns True whenever a rotation lands on 0."""

    def __init__(self):
        self._position: int = 50

    def turn_left(self, distance: int) -> bool:
        """True if landed on 0, False otherwise."""

        self._position = (self._position - distance) % 100
        #print(f"new position: ", self.position)
        return True if self._position == 0 else False

    def turn_right(self, distance: int) -> bool:
        """True if landed on 0, False otherwise."""

        self._position = (self._position + distance) % 100
        #print(f"new position: ", self._position)
        return True if self._position == 0 else False

class CounterDial:
    """Dial the counts how many times the dial touches 0."""

    def __init__(self):
        self._position: int = 50
        self._counter: int = 0

    def turn_left(self, distance: int) -> None:
        """Return the number of times the dial touched 0."""

        while distance > 0:
            # turn one tick left
            self._position -= 1
            if self._position == 0:
                self._counter += 1
            if self._position == -1:
                self._position = 99
            distance -= 1

    def turn_right(self, distance: int) -> None:
        """Return the number of times the dial touched 0."""

        while distance > 0:
            # turn one tick right
            self._position += 1
            if self._position == 0:
                self._counter += 1
            if self._position == 100:
                self._position = 0
                self._counter += 1
            distance -= 1

    @property
    def count(self) -> int:
        return self._counter

class Day01(DailyChallenge):
    """
    The first day's challenges.
    """

    def _part1(self, use_sample_data: bool=False) -> int:
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

    def _part2(self, use_sample_data: bool=False) -> int:
        data = self.part2_data if not use_sample_data else self.sample_data
        dial = CounterDial()
        rotations: list[str] = self.line_to_list(data, False)
        print(f"len rot= {len(rotations)}")
        for rotation in rotations:
            distance = int(rotation[1:])
            if rotation.startswith("L"):
                dial.turn_left(distance)

            elif rotation.startswith("R"):
                dial.turn_right(distance)

            else:
                raise ValueError(f"Expected 'L' or 'R', got {rotation[0]}")

        return dial.count
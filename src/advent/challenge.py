from abc import ABC, abstractmethod
from pathlib import Path

class DailyChallenge(ABC):
    """
    Configuration and data parsing for a daily challenge.
    """

    def __init__(self, part1: Path, part2: Path, sample: Path):
        self.part1_data = part1
        self.part2_data = part2
        self.sample_data = sample

    @abstractmethod
    def part1(self, use_sample_data: bool=False) -> int:
        pass

    @abstractmethod
    def part2(self) -> int:
        pass

    @property
    def sample(self) -> int:
        return self.part1(True)

    def line_to_list(self, data: Path, is_int: bool) -> list[int | str]:
        with open(data, "r", encoding="utf-8") as file:
            data_set = []
            if is_int:
                for line in file.readlines():
                    data_set.append(int(line.strip()))
            else:
                for line in file.readlines():
                    data_set.append(line.strip())

            print(f"{data_set=}")
            return data_set

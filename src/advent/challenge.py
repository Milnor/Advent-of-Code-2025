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
    def _part1(self, use_sample_data: bool=False) -> int:
        pass

    @abstractmethod
    def _part2(self, use_sample_data: bool=False) -> int:
        pass

    @property
    def part1(self) -> int:
        return self._part1()
    
    @property
    def part2(self) -> int:
        return self._part2()

    @property
    def sample1(self) -> int:
        return self._part1(True)

    @property
    def sample2(self) -> int:
        return self._part2(True)

    def line_to_list(self, data: Path, is_int: bool) -> list[int | str]:
        with open(data, "r", encoding="utf-8") as file:
            data_set = []
            if is_int:
                for line in file.readlines():
                    data_set.append(int(line.strip()))
            else:
                for line in file.readlines():
                    data_set.append(line.strip())

            return data_set

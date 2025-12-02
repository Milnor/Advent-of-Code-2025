"""Parent class for the daily challenges."""

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

    def csv_to_list(self, data: Path) -> list[str]:
        """
        Parse comma-separated values as a list of strings.
        """

        with open(data, "r", encoding="utf-8") as file:
            data_set = []
            for line in file.readlines():
                sublines = line.split(",")
                for subline in sublines:
                    if "-" in subline:
                        data_set.append(subline.strip())

            return data_set

    def line_to_list(self, data: Path) -> list[str]:
        """
        Parse each line into a list of strings.
        """

        with open(data, "r", encoding="utf-8") as file:
            data_set: list[str] = []
            for line in file.readlines():
                data_set.append(line.strip())

            return data_set

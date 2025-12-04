"""My solution to Day 4."""

from dataclasses import dataclass

from src.advent25 import DailyChallenge

THRESHOLD: int = 4 # Max adjacent rolls without obstructing forklift.

@dataclass
class Cell:
    value: str      # . or @
    adjacent: int   # count of adjacent rolls of paper

    def __str__(self):
        if self.value == '.':
            return '.'
        elif self.value == '@':
            return 'x' if self.adjacent <= THRESHOLD else '@'
        else:
            raise ValueError(f"Cell must contain . or @, not {self.value}")
    


class ForkliftMap:
    """Help forklifts find accessible rolls of paper easily."""

    def __init__(self, map_data: list[str]):
        # Map the raw data into a dictionary with adjacencies set to 0
        self.rows: dict[int, list[Cell]] = {}
        for index, data in enumerate(map_data, start=0):
            row: list[Cell] = []
            for character in data:
                row.append(Cell(character, 0))
            self.rows[index] = row

    def __str__(self):
        """Most useful for small sample datasets."""

        grid: str = ""
        for index, data in self.rows.items():
            current_row: str = f"{index:03d}  "
            for cell in data:
                current_row += str(cell)
            grid += current_row + "\n"

        return grid
    
    def update_adjacencies(self) -> None:
        """Visit every cell and calculate its adjacent rolls of paper."""

        last_row: int = len(self.rows) - 1
        last_col: int = len(self.rows[1]) - 1
        for row, data in self.rows.items():
            for col, cell in enumerate(data, start=0):
                count: int = 0
                # West and East
                if col > 0:
                    pass
                if col < last_col:
                    pass
                # NW, North, NE
                if row > 0:
                    pass
                # SW, South, SE
                if row < last_row:
                    pass
                cell.adjacent = count



    @property
    def accessible_count(self) -> int:
        """Return the number of accessible rolls of paper."""

        total: int = 0
        for row in self.rows.values():
            for cell in row:
                if cell.value == '@' and cell.adjacent < THRESHOLD:
                    total += 1

        return total

class Day04(DailyChallenge):
    """
    Day 4: Printing Department
    """

    def _part1(self, use_sample_data: bool=False) -> int:
        data = self.part1_data if not use_sample_data else self.sample_data
        forklift_map: list[str] = self.line_to_list(data)
        forkie = ForkliftMap(forklift_map)
        print(forkie)
        forkie.update_adjacencies()
        return forkie.accessible_count

    def _part2(self, use_sample_data: bool=False) -> int:
        return -1

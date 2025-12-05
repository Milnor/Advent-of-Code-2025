"""My solution to Day 4."""

from dataclasses import dataclass

from src.advent25 import DailyChallenge

_THRESHOLD: int = 4 # Max adjacent rolls without obstructing forklift.

@dataclass
class Cell:
    value: str      # . or @
    adjacent: int   # count of adjacent rolls of paper

    def __str__(self):
        if self.value == '.':
            return '.'
        elif self.value == '@':
            #return 'x' if len(self.adjacent.split(":")) < _THRESHOLD else '@'
            return 'x' if self.adjacent < _THRESHOLD else '@'
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
                #current_row += str(cell)
                current_row += f"{cell.value}{cell.adjacent} "
            grid += current_row + "\n"

        return grid
    
    def update_adjacencies(self) -> None:
        """Visit every cell and calculate its adjacent rolls of paper."""

        last_row: int = len(self.rows) - 1
        last_col: int = len(self.rows[1]) - 1

        for row in range(last_row + 1):
            for col in range(last_col + 1):
                count: int = 0
                #count: str = ""
                # Left
                if col > 0:
                    if self.rows[row][col - 1].value == '@':
                        #count += "L:"
                        count += 1

                # Right
                if col < last_col:
                    if self.rows[row][col + 1].value == '@':
                        #count += "R:"
                        count += 1

                # Up
                if row > 0:
                    if self.rows[row - 1][col].value == '@':
                        #count += "U:"
                        count += 1

                # Down
                if row < last_row:
                    if self.rows[row + 1][col].value == '@':
                        #count += "D:"
                        count += 1

                # Upper Left
                if row > 0 and col > 0:
                    if self.rows[row - 1][col - 1].value == '@':
                        #count += "UL:"
                        count += 1

                # Upper Right
                if row > 0 and col < last_col:
                    if self.rows[row - 1][col + 1].value == '@':
                        #count += "UR:"
                        count += 1

                # Lower Left
                if row < last_row and col > 0:
                    if self.rows[row + 1][col - 1].value == '@':
                        #count += "LL:"
                        count += 1

                # Lower Right
                if row < last_row and col < last_col:
                    if self.rows[row + 1][col + 1].value == '@':
                        #count += "LR"
                        count += 1

                self.rows[row][col].adjacent = count

    def remove_reachable(self) -> int:
        """
        Remove every accessible roll of paper and return how many rolls were
        removed with each pass.
        """
        last_row: int = len(self.rows) - 1
        last_col: int = len(self.rows[1]) - 1
        count: int = 0

        for row in range(last_row + 1):
            for col in range(last_col + 1):
                if self.rows[row][col].value == '@' and self.rows[row][col].adjacent < _THRESHOLD:
                    # Remove it with a fork lift!
                    self.rows[row][col] = Cell('.', 0)
                    count += 1

        return count


    @property
    def accessible_count(self) -> int:
        """Return the number of accessible rolls of paper."""

        total: int = 0
        for row in self.rows.values():
            for cell in row:
                if cell.value == '@' and cell.adjacent < _THRESHOLD:
                #if cell.value == '@' and len(cell.adjacent.split(':')) < _THRESHOLD:
                    total += 1

        return total

    # @property
    # def inaccessible_count(self) -> int:
    #     """Return the number of inaccessible rolls of paper."""

    #     total: int = 0
    #     for row in self.rows.values():
    #         for cell in row:
    #             if cell.value == '@' and cell.adjacent >= _THRESHOLD:
    #                 total += 1

    #     return total


class Day04(DailyChallenge):
    """
    Day 4: Printing Department
    """

    def _part1(self, use_sample_data: bool=False) -> int:
        data = self.part1_data if not use_sample_data else self.sample_data
        forklift_map: list[str] = self.line_to_list(data)
        forkie = ForkliftMap(forklift_map)
        #print(forkie)
        forkie.update_adjacencies()
        #print(forkie)
        return forkie.accessible_count

    def _part2(self, use_sample_data: bool=False) -> int:
        data = self.part1_data if not use_sample_data else self.sample_data
        forklift_map: list[str] = self.line_to_list(data)
        forkie = ForkliftMap(forklift_map)
        forkie.update_adjacencies()
        total: int = 0

        while True:
            removed = forkie.remove_reachable()
            total += removed
            #print(f"{removed=}")
            if removed == 0:
                return total
            forkie.update_adjacencies()

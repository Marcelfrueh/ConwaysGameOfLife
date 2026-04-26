from collections import Counter
from typing import Set, Tuple

DIRECTIONS = [
    (-1, -1), (-1, 0),
    (-1, 1), (0, -1),
    (0, 1), (1, -1),
    (1, 0), (1, 1)
    ]

class Game:
    def __init__(self, initial_cells: Set[Tuple[int, int]], rows: int, cols: int):
        self.cells = initial_cells
        self.rows = rows
        self.cols = cols
        self._generation = 0

    @property
    def generation(self) -> int:
        return self._generation

    def _count_neighbours(self) -> Counter:
        neighbour_counts = Counter()
        for row, col in self.cells:
            for dir_row, dir_col in DIRECTIONS:
                neighbour_counts[(row + dir_row, col + dir_col)] += 1
        return neighbour_counts

    def next_generation(self) -> None:
        neighbour_counts = self._count_neighbours()
        new_alive_cells = set()

        for cell_coords, count in neighbour_counts.items():
            row, col = cell_coords

            if 0 <= row < self.rows and 0 <= col < self.cols:
                # rule 1: live cell lives if 2 or 3 neighbors
                # rule 2: dead cell lives if 3 neighbors
                # else dead
                if count == 3 or (count == 2 and cell_coords in self.cells):
                    new_alive_cells.add(cell_coords)

        self.cells = new_alive_cells
        self._generation += 1


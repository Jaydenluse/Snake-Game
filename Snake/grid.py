import numpy as np
from enum import Enum

class CellType(Enum):
    EMPTY = 1
    SNAKE = 2
    FOOD = 3
    TOKEN = 4

class Grid:
    _cells: dict[CellType, set]
    _grid: any


    def __init__(self) -> None:
        self.resetGrid()

    def cells(self):
        interimCells = []
        for cellType in CellType:
            interimCells.extend(list(self._cells[cellType]))

        return interimCells
        

    def reserveCells(self, cells, type) -> None:
        for cell in cells:
            if (cell not in self.getCells(CellType.EMPTY)):
                self.getCells(CellType.EMPTY).remove(cell)
                self._cells[type].add(cell)

        # if (in self.emptyCells())

        for cell in cells:
            self._grid[cell[0], cell[1]] = type

    def getCells(self, cellType) -> set:
        return self._cells[cellType]

    def getGrid(self) -> any:
        return self._grid

    def resetGrid(self) -> None:
        self._cells = {
            CellType.EMPTY: set(),
            CellType.SNAKE: set(),
            CellType.FOOD: set(),
            CellType.TOKEN: set()
        }

        for x in range(20):
            for y in range(20):
                self._cells[CellType.EMPTY].add((x, y))

        self._grid = np.full((20,20), CellType.EMPTY)

    def test(self):
        print(self._cells[CellType.EMPTY])
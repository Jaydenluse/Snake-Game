from grid import CellType
from constants import WHITE, GREEN, GOLD, RED

def transformTypeToColor(type: CellType):
    if (type == CellType.EMPTY):
        return WHITE
    elif (type == CellType.SNAKE):
        return GREEN
    elif (type == CellType.FOOD):
        return RED
    elif (type == CellType.TOKEN):
        return GOLD

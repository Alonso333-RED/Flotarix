class Square:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.ship_inside = None

class Board:
    def __init__(self, xsize: int, ysize: int):
        self.xsize = xsize
        self.ysize = ysize

        self.grid = [
            [Square(x, y) for x in range(xsize)]
            for y in range(ysize)
        ]

    def get_square(self, x: int, y: int) -> Square | None:
        if 0 <= x < self.xsize and 0 <= y < self.ysize:
            return self.grid[y][x]
        return None
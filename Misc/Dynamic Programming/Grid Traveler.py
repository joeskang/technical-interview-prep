"""
given a m x n grid, how many ways can I go from the top left to the bottom right space?

ie. 2x3 grid:
answer = 3 ways
* Right right down
* Right down right
* Down right right

"""


def gridTraveler( row: int, col: int ) -> int:

    cache = {} # keys: coordinate, values: count

    def explore(x, y) -> int:
        if (x,y) in cache:
            return cache[(x,y)]
        if 0 in (x, y):
            return 0
        if x == y == 1:
            return 1

        count = sum((explore(x - 1, y), explore(x, y - 1)))
        cache[(x,y)] = count
        return count

    return explore(row, col)

if __name__ == '__main__':
    print(gridTraveler(18, 18))
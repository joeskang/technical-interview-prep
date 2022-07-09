def removeIslands(matrix):
    # 1 = black
    # 0  = white

    cache = {}
    islands = []

    def good_island(x, y, island_num):

        if (x, y) in cache:
            return cache[(x,y)]

        if matrix[x][y] != 1:
            return True

        # else, it's a 1
        # check to see if at an edge
        if x in (len(matrix)-1, 0) or y in (len(matrix)-1, 0):

            cache[(x,y)] = island_num
            return False

        # else, it's one and we can continue
        status = good_island(x+1, y) and good_island(x, y+1)
        cache[(x,y)] = island_num
        islands[island_num] = status
        return


    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            if (m, n) not in cache:
                # cache[(m, n)] = good_island(m, n)
                island_num = len(islands)
                cache[(m, n)] = island_num
                islands.append(False)
                good_island(m, n, island_num)

    # finally find all the 1's to execute
    for k, v in cache.items():
        if islands[v]:
            x, y = k
            matrix[x][y] = 0

    return matrix

if __name__ == "__main__":
    mymatrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    print(removeIslands(mymatrix))

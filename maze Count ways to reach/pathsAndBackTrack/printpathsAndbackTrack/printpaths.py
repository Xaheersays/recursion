grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
path = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]


def pathInArrayAndBackTrack(pro, row, col, grid, path, step):
    if row == len(grid) - 1 and col == len(grid) - 1:
        path[row][col] = step
        for p in path:
            print(p)
        # print(path)
        print(pro)
        # path[row][col]=-1
        print()
        return
    if not grid[row][col]:
        return
    grid[row][col] = 0
    path[row][col] = step
    if row < len(grid) - 1:
        pathInArrayAndBackTrack(pro + "D", row + 1, col, grid, path, step + 1)

    if col < len(grid) - 1:
        pathInArrayAndBackTrack(pro + "R", row, col + 1, grid, path, step + 1)

    if row > 0:
        pathInArrayAndBackTrack(pro + "U", row - 1, col, grid, path, step + 1)

    if col > 0:
        pathInArrayAndBackTrack(pro + "B", row, col - 1, grid, path, step + 1)

    grid[row][col] = 1
    path[row][col] = -1


print(pathInArrayAndBackTrack("", 0, 0, grid, path, 1))

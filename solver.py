board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# board = [
#     [5, 3, 1, 1, 7, 1, 1, 1, 1],
#     [6, 1, 1, 1, 9, 5, 1, 1, 1],
#     [1, 9, 8, 1, 1, 1, 1, 6, 1],
#     [8, 1, 1, 1, 6, 1, 1, 1, 3],
#     [4, 1, 1, 8, 1, 3, 1, 1, 1],
#     [7, 1, 1, 1, 2, 1, 1, 1, 6],
#     [1, 6, 1, 1, 1, 1, 2, 8, 1],
#     [1, 1, 1, 4, 1, 9, 1, 1, 5],
#     [1, 1, 1, 1, 8, 1, 1, 7, 9]
# ]


def printBoard(board):
    for i in board:
        print(i)
    print()


def findOpen(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return False


def checkBox(board, x, y, num):
    xMin = xMax = yMin = yMax = 0
    if x < 3:
        xMin = 0
        xMax = 3
    elif 3 <= x < 6:
        xMin = 3
        xMax = 6
    elif x > 6:
        xMin = 6
        xMax = 9

    if y < 3:
        yMin = 0
        yMax = 3
    elif 3 <= y < 6:
        yMin = 3
        yMax = 6
    elif y > 6:
        yMin = 6
        yMax = 9

    print(f"{xMin}, {xMax}, {yMin}, {yMax}")
    # checks left 3 big boxes
    for i in range(xMin, xMax):
        for j in range(yMin, yMax):
            if num == board[i][j]:
                return False
    return True


def check(board, x, y, num):
    if num in board[x]:
        # print("hello")
        return False

    for i in range(len(board)):
        if board[i][y] == num:
            return False

    if checkBox(board, x, y, num) == False:
        return False

    return True


def solve(board):
    # creates tuple with x,y coordinates of empty space(0) in a list
    find = findOpen(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1, 10):
        # checks to see what number works, then places it
        if check(board, row, col, i):
            board[row][col] = i
            printBoard(board)
            break

    # then see if solve(board) is true
    # Base statement
    if solve(board):
        return True
    board[row][col] = 0

    return False


# print(checkBox(board, 1, 2, 3))
print(solve(board))

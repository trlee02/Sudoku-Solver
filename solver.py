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


def printBoard(board):
    for i in board:
        print(i)


'''
    find an open slot
    if all slots are full
        return true                 base condition

    try to fill slot with a number
    if it is filled
        solve(board)                recursion condition
    else
        return false

    '''


def findOpen(board):
    for i in range(len(board)):
        if 0 in board[i]:
            x = i
            y = board[i].index(0)
            return x, y
        else:
            return -1


def checkBox(board, x, y, num):
    xMin = xMax = yMin = yMax = 0
    if x < 2:
        xMin = 0
        xMax = 3
    elif 2 < x < 6:
        xMin = 3
        xMax = 6
    elif x > 6:
        xMin = 6
        xMax = 9

    if y < 2:
        yMin = 0
        yMax = 3
    elif 2 < y < 6:
        yMin = 3
        yMax = 6
    elif y > 6:
        yMin = 6
        yMax = 9

    # checks left 3 big boxes
    for i in range(xMin, xMax):
        for j in range(yMin, yMax):
            if num == board[i][j]:
                return False
    print("works!")
    return True


def check(board, x, y, num):
    if num in board[x]:
        return False

    for i in range(len(board)):
        if board[i][y] == num:
            return False

    if not checkBox(board, x, y, num):
        return False

    return True


def solve(board):
    # creates tuple with x,y coordinates of empty space(0) in a list
    find = findOpen(board)
    if find == -1:      # base statement
        return True

    for i in range(1, 9):
        # checks to see what number works, then places it
        if check(board, find[0], find[1], i):
            board[find[0]][find[1]]
        #
        # then see if solve(board) is true
        # Base statement


printBoard(board)
print(check(board, 1, 1, 8))
# print(solve(board))

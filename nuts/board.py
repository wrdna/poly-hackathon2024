import copy
import opencv

def main():
    size = 200 

    b = readBoard('nuts.dat')
    spos = getSquirrelPos(b, size)
    fss = findSingles(b, size)
    print(fss)

    #saveBoard(b, size)b
# Create a N x N solved puzzle
def readBoard(filename):
    board = []
    with open(filename, 'r') as f:
        for line in f.readlines()[3:]:
            board.append([*line])
    return board

# Get coordinates of squirrel
def getSquirrelPos(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == '@':
                return (i,j)
    print('Error: getSquirrelPos')
    print('Could not find squirrel')
    exit(1)

def findSingles(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j].isdigit():
                if isAlone(board, i, j):
                    print(i, j)
    print('Error: getSquirrelPos')
    print('Could not find squirrel')
    exit(1)

def isAlone(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in neighbors:
        new_row, new_col = rows + dx, cols + dy
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col].isdigit():
            return False
    return True


def saveBoard(board, size):
    with open("output.txt", "w") as file:
        # Write the three-dimensional array to the file
        for i in range(size):
            for j in range(size):
                file.write(f"{board[i][j]}")
            file.write("\n")  

# Return a list of valid moves per squirrel location
def getValidMoves(n, squirrelPos):
    squirrely = squirrelPos[0]
    squirrelx = squirrelPos[1]
    validmoves = []

    if squirrelx != 0:
        validmoves.append('W')
    if squirrelx != n-1:
        validmoves.append('E')
    if squirrely != 0:
        validmoves.append('N')
    if squirrely != n-1:
        validmoves.append('S')

    return validmoves

# Make a move and return the board
def makeMove(move, squirrelPos, holding, current_board):
    board = copy.deepcopy(current_board)

    squirrely = squirrelPos[0]
    squirrelx = squirrelPos[1]

    if move == 'W':
        squirrelPos = (squirrely, squirrelx-1)
    elif move == 'E':
        squirrelPos = (squirrely, squirrelx+1)
    elif move == 'N':
        squirrelPos = (squirrely-1, squirrelx)
    elif move == 'S':
        squirrelPos = (squirrely+1, squirrelx)
    elif move == 'P' and not holding:
        board[squirrely][squirrelx] -= 1
        holding = True
    elif move == 'D':
        board[squirrely][squirrelx] += 1
        holding = False
    

    return board, squirrelPos

if __name__ == "__main__":
    main()

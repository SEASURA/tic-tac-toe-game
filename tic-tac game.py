from random import randrange

def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|", end="")
        for cell in row:
            print(f"   {cell}   |", end="")
        print()
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
        except ValueError:
            print("Invalid input. Enter a number 1-9.")
            continue
        if move < 1 or move > 9:
            print("Number must be between 1 and 9.")
            continue
        row, col = (move - 1) // 3, (move - 1) % 3
        if board[row][col] in ('X', 'O'):
            print("That square is already taken.")
            continue
        board[row][col] = 'O'
        break

def make_list_of_free_fields(board):
    return [(r, c) for r in range(3) for c in range(3)
            if board[r][c] not in ('X', 'O')]

def victory_for(board, sign):
    wins = [
        [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)],
    ]
    return any(all(board[r][c] == sign for r, c in line) for line in wins)

def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'

# Initialize board with square numbers
board = [[str(r*3+c+1) for c in range(3)] for r in range(3)]

# Computer's first move: center
board[1][1] = 'X'
display_board(board)

while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("You won!")
        break
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break

    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("Computer wins!")
        break
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
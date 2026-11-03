import random
board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
def display_board(board) :
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        print("|", end="")
        for col in range(3):
            print("   " + str(board[row][col]) + "   |", end="")
        print()
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board) :
    while True:
        try:
            move = int(input("Enter your move: "))

            if move < 1 or move > 9:
                print("Invalid move! Enter a number from 1 to 9.")
                continue

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] in ["X", "O"]:
                print("This field is already occupied!")
                continue

            board[row][col] = "O"
            break

        except ValueError:
            print("Invalid input! Enter an integer.")




def make_list_of_free_fields(board):
    free = []

    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["X", "O"]:
                free.append((row, col))

    return free


def victory_for(board, sign):
    # Verifier les lignes
    for row in range(3):
        if (board[row][0] == sign and
            board[row][1] == sign and
            board[row][2] == sign):
            return True

    # Verifier les colonnes
    for col in range(3):
        if (board[0][col] == sign and
            board[1][col] == sign and
            board[2][col] == sign):
            return True

    # Verifier la diagonale principale
    if (board[0][0] == sign and
        board[1][1] == sign and
        board[2][2] == sign):
        return True

    # Verifier la diagonale secondaire
    if (board[0][2] == sign and
        board[1][1] == sign and
        board[2][0] == sign):
        return True

    return False



def draw_move(board):
    free = make_list_of_free_fields(board)

    if len(free) > 0:
        index = random.randrange(len(free))
        row, col = free[index]

        board[row][col] = "X"
        
        


# 7. Programme principal

# Le premier coup appartient a l'ordinateur
board[1][1] = "X"

display_board(board)

while True:

    # Coup de l'utilisateur
    enter_move(board)
    display_board(board)

    # Verifier si l'utilisateur a gagne
    if victory_for(board, "O"):
        print("You won!")
        break

    # Verifier si le plateau est plein
    if len(make_list_of_free_fields(board)) == 0:
        print("It's a tie!")
        break

    # Coup de l'ordinateur
    draw_move(board)
    display_board(board)

    # Verifier si l'ordinateur a gagne
    if victory_for(board, "X"):
        print("Computer won!")
        break

    # Verifier si le plateau est plein
    if len(make_list_of_free_fields(board)) == 0:
        print("It's a tie!")
        break

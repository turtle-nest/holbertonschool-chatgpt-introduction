#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérifie les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]  # Retourne le gagnant (X ou O)

    # Vérifie les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Vérifie la diagonale principale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    # Vérifie la diagonale secondaire
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None  # Pas de gagnant

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    winner = None

    while not winner and not is_full(board):
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in range(3) or col not in range(3):
                print("Invalid input! Please enter 0, 1, or 2.")
                continue
            if board[row][col] == " ":
                board[row][col] = player
                winner = check_winner(board)
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 2.")

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()

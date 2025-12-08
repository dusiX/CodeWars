# Take a look at wiki description of Connect Four game:

# Wiki Connect Four

# The grid is 6 row by 7 columns, those being named from A to G.

# You will receive a list of strings showing the order of the pieces which dropped in columns:

#   pieces_position_list = ["A_Red",
#                           "B_Yellow",
#                           "A_Red",
#                           "B_Yellow",
#                           "A_Red",
#                           "B_Yellow",
#                           "G_Red",
#                           "B_Yellow"]
# The list may contain up to 42 moves and shows the order the players are playing.

# The first player who connects four items of the same color is the winner.

# You should return "Yellow", "Red" or "Draw" accordingly.

def who_is_winner(pieces_position_list):
    columns = {
        "A" : 0,
        "B" : 1,
        "C" : 2,
        "D" : 3,
        "E" : 4,
        "F" : 5,
        "G" : 6
    }
    
    board = [[0 for _ in range(7)] for _ in range(6)]
    
    def check_win(board, color):
        for r in range(3):
            for c in range(7):
                if (board[r][c] == color and board[r+1][c] == color and 
                    board[r+2][c] == color and board[r+3][c] == color):
                    return True
        
        for r in range(6):
            for c in range(4):
                if (board[r][c] == color and board[r][c+1] == color and
                    board[r][c+2] == color and board[r][c+3] == color):
                    return True
        
        for r in range(3, 6):
            for c in range(4):
                if (board[r][c] == color and board[r-1][c+1] == color and
                    board[r-2][c+2] == color and board[r-3][c+3] == color):
                    return True
        
        for r in range(3):
            for c in range(4):
                if (board[r][c] == color and board[r+1][c+1] == color and
                    board[r+2][c+2] == color and board[r+3][c+3] == color):
                    return True
        
        return False

    for move in pieces_position_list:
        col_letter, color = move.split("_")
        col = columns[col_letter]

        for row in range(6):
            if board[row][col] == 0:
                board[row][col] = color
                break

        if check_win(board, color):
            return color

    return "Draw"
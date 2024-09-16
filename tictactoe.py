input_row = "Please select a row by typing number 0, 1 or 2"
input_col = "Please select a column by typing number 0, 1 or 2"
print_player = "You are player {} and your sign is {}"
print_win = "Player {} won."
print_draw = "Draw!"

row_print = "| {} | {} | {} |"
col_seperator = " ___________"
game = None

signs = ['X','O']
player1_active = True
game_active = True
diagonal_entries = [[0,0],[1,1],[2,2],[0,2],[2,0]]
diagonal1 = [[0,0], [1,1], [2,2]]
diagonal2 = [[0,2], [1,1], [2,2]]

# The class move describes a valid. move. 
class Move:
    row = None
    col = None
    player_sign = None
    
    def __init__(self, row, col, player_sign):
        if row < 3 and row >= 0:
            self.row = row
        else:
            raise ValueError('Invalid row')
        if col < 3 and col >= 0:
            self.col = col
        else:
            raise ValueError('Invalid column')
        if player_sign == 'X' or player_sign == 'O':
            self.player_sign = player_sign
        else:
            raise ValueError('Invalid sign')
    
# The class Game holds the state of the game. When initialized it contains an empty field, and gets updated with each move
class Game:
    entries = []
    active = True
    draw = False
    
    # the field is initialized with 3 columns and 3 rows like a regular tic tac toe game. This could be changed in the future for different sizes of playing fields.
    def __init__(self, rows = 3, cols = 3):
        self.entries = [[' ' for x in range(rows)] for y in range(cols)]
    
    # The function apply_move takes a move of type Move and applies it to the field, if its valid. Otherwise, an error is raised.
    def apply_move(self, move: Move):
        if (self.entries[move.row][move.col] != ' '):
            raise ValueError('Invalid move')    
        self.entries[move.row][move.col] = move.player_sign
        self.draw = self.check_full()
        if (self.check_win(move) or self.draw):
            self.active = False
    
    # This function checks for all possible win conditions: same player symbol in the row of the move, same player symbol in the column of the move, or same symbol in the diagonals.    
    def check_win(self, move: Move):
        if (self.entries[move.row][0] == self.entries[move.row][1] == self.entries[move.row][2] == move.player_sign):
            return True
        if (self.entries[0][move.col] == self.entries[1][move.col] == self.entries[2][move.col] == move.player_sign):
            return True
        if ([move.row, move.col] in diagonal1):
            if (self.entries[0][0] == self.entries[1][1] == self.entries[2][2] == move.player_sign):
                return True
        if ([move.row, move.col] in diagonal1):
            if (self.entries[0][2] == self.entries[1][1] == self.entries[2][0] == move.player_sign):
                return True
        return False
    
    # This is used to check if all fields are filled with symbols. If there is no win, this is a draw and the game should end.
    def check_full(self):
        for row in self.entries:
            for entry in row:
                if entry != 'X' and entry != 'O':
                    return False
        return True
        
        
# This function is used to print the game state       
def print_game(game: Game):
    for row in game.entries:
        print(col_seperator)
        print(row_print.format(row[0], row[1], row[2]))
    print(col_seperator)

# The function ask_usermove takes a game state as input and asks the active player to make a move. This is done until there is a valid move, which is applied to the game state.
def ask_usermove(game: Game):
    global player1_active
    global signs
    valid = False
    
    print(print_player.format(int(player1_active), signs[int(player1_active)]))
    while not valid:
        print(input_row)
        row = int(input())
        print(input_col)
        col = int(input())
    
        try:
            move = Move(row, col, signs[int(player1_active)])
            game.apply_move(move)
            break
        except ValueError:
            print("Your move was not a legal move, please try again.")

    return game

   
    
        

def main():
    global game, game_active, player1_active
    game = Game()
    print_game(game)
    while game.active:
        game = ask_usermove(game)
        print_game(game)
        # this condition checks if the end of the game is reached, either because there is a win or a draw
        if not game.active:
            break
        # if the game continues, switch the active player
        player1_active = not player1_active
    # announce a draw or the winning player
    if (game.draw):
        print(print_draw)
    else:
        print(print_win.format(int(player1_active)))
        

if __name__ == "__main__":
    main()
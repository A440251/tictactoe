"""
Welcome to Tic Tac Toe!

Dictionary taken from http://thepixiepit.co.uk/scrabble/CSW12.txt

Please input an answer:

An answer of "!STARTAI" will play against the computer.
An answer of "!START2P" will start a game for two players.
An answer of "!QUIT" will quit the game.

"""
#The current_state is what the board looks like. It is a list that contains
#three lists that represent each row of the tic-tac-toe board
#current_state[row][column] accesses the value at that position in the matrix
current_state = [["-", "-", "-"] for i in range(3)]
print (current_state)

def draw_board(board):
    print()
    print((" %s | %s | %s ") % (board[0][0], board[0][1], board[0][2]))
    print("-----------")
    print((" %s | %s | %s ") % (board[1][0], board[1][1], board[1][2]))
    print("-----------")
    print((" %s | %s | %s ") % (board[2][0], board[2][1], board[2][2]))
    print()
    
def welcome():
    #__doc__ is the header in triple quotes 'Welcome to Tic Tac Toe!...'
    print (__doc__)
def main():
    welcome()
    done = False
    #This while loop ensures that we keep going on with the game as
    #long as we are not done playing!
    while not done:
        answer = input("What is your answer?\n...>")
        if answer.upper() == "!STARTAI":
            START_AI()
        if answer.upper() == "!START2P":
            START_2P()
        if answer.upper() == "!QUIT":
            break
    print ("Thanks for trying TIC TAC TOE! Goodbye!")
    
            

##best practice, see
##http://stackoverflow.com/questions/419163/what-does-if-name-main-do
##for details
if __name__ == "__main__":
    main()

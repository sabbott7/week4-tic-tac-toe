def printBoard(board):
    
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################

    #Given a board and a player’s letter, this function returns True if that player has won.

    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or # across the top 
    (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or # across the middle
    (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or # across the bottom
    (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or # down the left side
    (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or # down the middle
    (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or # down the right side
    (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or # diagonal
    (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player)) # diagonal

    #end of CheckWinner function    
    
def startGame(startingPlayer, board): # define function with 2 parameters
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer # active player 1st to make choice
    for i in range(9): #loops through all the 9 board key locations for each turn
        printBoard(board) # prints out the board at the start of each turn
        print('Turn for ' + turn + '. Move on which space?') #output to screen active player name
        move = input() # extracts the active players move
        board[move] = turn # updates the value for the key in the board
        if( checkWinner(board, 'X') ): #calls to checkWinner func return type=True where player 'X' has won
            print('X wins!') # output to screen player 'X' won game
            break # exit program 
        elif ( checkWinner(board, 'O') ): # calls to checkWinner func return=True where player 'O' has won
            print('O wins!') # output to screen player 'X' won game
            break # exit program
    
        if turn == 'X': # check condition for current player = 'X'
            turn = 'O' # if active player = 'X' then swap to player 'O'
        else:
            turn = 'X' # active player = 'O' therefore swap to player 'X' 
        
    printBoard(board)
    

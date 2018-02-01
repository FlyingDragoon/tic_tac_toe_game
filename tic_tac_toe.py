# configuration

import random
import os

# create a utility function
# clear screen when run on terminal
def clear():
    tmp_var = os.system('clear')
    tmp_var = tmp_var
    return()

# step 1: create a grid
grid = [ [" "," "," "]
        ,[" "," "," "]
        ,[" "," "," "]
        ]

def print_grid(grid):
    '''
    print out the game board
    '''
    clear()
    i = 0
    for row in grid:
        #print '\n'
        #for i in range(0, len(row)):
        print '%s | %s | %s' %(row[0],row[1], row[2])
        i += 1
        if i < len(grid) :
            print '- - - - -'
    return()

# test
#print_grid(grid)
    
# step 1.2: decide turn and mark type
def decide_turn(): #decide turn randomly
    if bool(random.getrandbits(1)):
        turn = 1
    else:
        turn = 2
    return(turn)

def decide_mark_type(): #decide mark type randomly
    if bool(random.getrandbits(1)):
        mark_type = 'X'
    else:
        mark_type = 'O'
    return mark_type

# step 2: place a mark
def place_mark(row_num, col_num, mark_type, grid):
    grid[row_num - 1][col_num - 1] = mark_type
    return(grid)

# step 2, add.1: check if the board is full
def check_full(grid):
    indicator = grid[0].count(" ") + grid[1].count(" ") + grid[2].count(" ")
    if indicator == 0:
        return True
    else:
        return False
# step 2, add.2: check if the mark placed already has a mark there
def check_if_marked(row_num, col_num):
    if grid[row_num-1][col_num-1] != " ":
        return True
    else:
        return False
    

# test
#grid_test_1 = place_mark(1,1,'*',grid)
#print_grid(grid_test_1)
    
#new_grid = place_mark(3,3,'*',grid)
#print_grid(new_grid)

# step 3: determine winning or not
# 
def check_win(grid):
    '''
    there are 3 scenarios where winning can happen
    1-same on a row
    2-same on a column
    3-same on a diagal line    
    '''
    # one identical row
    if grid[0][0] == grid[0][1] == grid[0][2]!= ' ':
        return(True)
    elif grid[1][0] == grid[1][1] == grid[1][2]!= ' ':
        return(True)
    elif grid[2][0] == grid[2][1] == grid[2][2]!= ' ':
        return(True)
    # one identical column
    elif grid[0][0] == grid[1][0] == grid[2][0]!= ' ':
        return(True)
    elif grid[0][1] == grid[1][1] == grid[2][1]!= ' ':
        return(True)
    elif grid[0][2] == grid[1][2] == grid[2][2]!= ' ':
        return(True)
    # diagnal
    elif grid[0][0] == grid[1][1] == grid[2][2]!= ' ':
        return(True)
    elif grid[0][2] == grid[1][1] == grid[2][0]!= ' ':
        return(True)
    else:
        return(False)
    
# below is main function which begins the game
# add added items to main function 
def main(grid, replay='Y'):
    '''
    this is the main function that starts the game
    '''
    while replay == 'Y':     
        i = 1
        total_moves = len(grid) * len(grid[0])
        # decide turn: player 1 or 2 to move first
        first_player = decide_turn()
        print 'player %1.0f moves first' %(first_player)
        # decide mark type for the first player
        mark_type_1 = decide_mark_type()
        if mark_type_1 == 'X':
            mark_type_2 = 'O'
        elif mark_type_1 == 'O':
            mark_type_2 = 'X'
        else:
            pass
        print 'mark type for player %1.0f is %s, for player %1.0f is %s' %(first_player, mark_type_1, 3-first_player, mark_type_2)     
       
        for i in range(1, total_moves+1):
            print '\nmove %1.0f' %(i)
            
            # check if the board is full
            if check_full(grid):
                print 'board is full'
                replay = bool(raw_input('Replay? True/False '))
                break
            
            # acceipt interactive input, with a few checks reinforced
            while True:
                try:
                    mark_row = int(raw_input('input your mark row: '))
                    mark_col = int(raw_input('input your mark col: '))
                    if mark_row > 3 or mark_col > 3: # check if inputs are within range
                        print 'row/column number cannot be greater than 3, please try again'
                        continue
                    if check_if_marked(mark_row, mark_col): # check if the position has already been marked
                        print 'the position you selected is already marked, please try again'
                        continue
                except:
                    print 'an error occured; please try again'
                    continue
                else:
                    break
            
            if i % 2 == 1: # first move player's turn
                mark_type = mark_type_1
            elif i % 2 == 0: # second move player's turn
                mark_type = mark_type_2
                
            grid = place_mark(mark_row,mark_col,mark_type,grid)        
            print_grid(grid)    
            
            if check_win(grid):
                print 'you win! gg!'
                break
            elif i == total_moves:    
                print 'it\'s a tie!'
                break
            else:
                pass
            i += 1
            
        replay = raw_input('Replay? Y/N ')
        
    return()

# run the game
main(grid)

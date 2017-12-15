# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
#os.getcwd()

path = '/Users/yabinwang/Desktop/py_dir/'
os.chdir(path)
#print os.getcwd()

'''
rules of tic tac toe

the games happens on a 3*3 grid
players take turns placing mark on the grid
each player can ohly place one mark in each turn
whoever has three marks horizontally, vertically, or diagnolly wins 
'''

'''
some other requirements:

2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board
'''

'''
step 1: get a grid
grid -> list of list

step 2: place mark
two numeric inputs can determine mark in grid

step 3: dertermine winning side
compile all cases of winning mark positions; if is in one of these, then win
'''

# step 1: create a grid
grid = [ [" "," "," "]
        ,[" "," "," "]
        ,[" "," "," "]
        ]

def print_grid(grid):
    '''
    print out the game board
    '''
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

# step 2: place a mark
def place_mark(row_num, col_num, mark_type, grid):
    grid[row_num - 1][col_num - 1] = mark_type
    return(grid)

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
def main(grid):
    '''
    this is the main function that starts the game
    '''
    i = 1
    total_moves = len(grid) * len(grid[0])
    for i in range(1, total_moves+1):
        print '\nmove %1.0f by player %1.0f' %(i, (i - 1) % 2 + 1)
        # change to be interactive input
        mark_row = int(raw_input('input your mark row: '))
        mark_col = int(raw_input('input your mark col: '))
        if i % 2 == 0:
            mark_type = '*'
        else:
            mark_type = '#'
        
        grid = place_mark(mark_row,mark_col,mark_type,grid)        
        print_grid(grid)    
        
        if check_win(grid):
            print 'you win! gg!'
            break
        elif i == total_moves:    
            print 'it\'s a tie!'
        else:
            pass
        
        i += 1
    return()

'''
[CH!!!] 
save this via git
read full-walk-through
    -features to add
        -lets player decide the mark type s/he wants to select
        -determine which player wants to move first (using random module)
        -check if the board already has mark placed        
        -check if the board is full
        -adding replay feature (i.e., can replay the entire game)
        
'''

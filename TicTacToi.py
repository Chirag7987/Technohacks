# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 18:42:44 2023

@author: HP
"""

import numpy
board=numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
ps1='X'
ps2='O'
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            print(symbol,'win')
            return True
        
def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            print(symbol,'win')
            return True
    return False

def check_diagonals(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    return False
def won(symbol):
    return check_rows(symbol) and check_cols(symbol) and check_diagonals(symbol)
def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input('Enter the rows - 1, 2 and 3'))
        col=int(input('Enter the cols - 1, 2 and 3'))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='_':
            break
        else:
            print("invalid input,try again")
    board[row-1][col-1]=symbol        
def play():
    for turn in range(9):
        if turn%2==0:
            print('X turn')
            place(ps1)
            if won(ps1):
                break
        else:
            print('O turn')
            place(ps2)
            if won(ps2):
                break
    if not(won(ps1)) and not(won(ps2)):
        print('Draw')
    







play()


    
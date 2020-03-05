from tkinter import *


def listener(r, c):
    global player, board
    if button[r][c].cget('text') == ' ':
        button[r][c].configure(text=player)

        p = 3 * r + c
        board = board[:p] + (player, ) + board[p + 1:]

        player = 'X' if player == 'O' else 'O'
        w = check_winner(board)
        if w == 'X':
            print('X wins')
        elif w == 'O':
            print('O Wins')
        elif w == 'D':
            print('Draw')


def check_winner(B):
    if B[0] == B[1] == B[2] != ' ':
        return B[0]
    if B[3] == B[4] == B[5] != ' ':
        return B[3]
    if B[6] == B[7] == B[8] != ' ':
        return B[6]

    if B[0] == B[3] == B[6] != ' ':
        return B[0]
    if B[1] == B[4] == B[7] != ' ':
        return B[1]
    if B[2] == B[5] == B[8] != ' ':
        return B[2]

    if B[0] == B[4] == B[8] != ' ':
        return B[0]
    if B[2] == B[4] == B[6] != ' ':
        return B[2]

    if B.count(' ') == 0:
        return 'D'

    return 'N'


root = Tk()
root.title('Tic-Tac-Toe')

button = [[0]*3 for i in range(3)]
for r in range(3):
    for c in range(3):
        B = Button(text=' ', font =('Courier New', 72), bg='#ffffff', command = lambda r=r, c=c:listener(r, c))
        B.grid(row=r, column=c)
        button[r][c] = B

player = 'X'

board = (' ',) * 9

mainloop()
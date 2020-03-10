from tkinter import *
from tkinter.messagebox import *


MAX = 1
MIN = 2


def listener(r, c):
    global player, board
    if button[r][c].cget('text') == ' ':
        button[r][c].configure(text=player)

        p = 3 * r + c

        board = board[:p] + (player, ) + board[p + 1:]
        root.update()

        w = check_winner(board)
        if w == 'X':
            showinfo(title='Game Over', message='X Wins!!!')
            exit()
        elif w == 'O':
            showinfo(title='Game Over', message='O Wins!!!')
            exit()
        elif w == 'D':
            showinfo(title='Game Over', message="It's a Draw...")
            exit()

        player = 'O'
        spot = choose_move(board, MIN)
        print(spot)

        r, c = spot // 3, spot % 3
        button[r][c].configure(text=player)
        p = 3 * r + c
        board = board[:p] + (player,) + board[p + 1:]

        w = check_winner(board)
        if w == 'X':
            showinfo(title='Game Over', message='X Wins!!!')
            exit()
        elif w == 'O':
            showinfo(title='Game Over', message='O Wins!!!')
            exit()
        elif w == 'D':
            showinfo(title='Game Over', message="It's a Draw...")
            exit()
        player = 'X'
        #print(choose_move(board, MAX))




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


def minimax(v, player):
    c = check_winner(v)
    if c != 'N':
        util = {'X': 10, 'O': -10, 'D': 0}
        return util[c]

    spots = [i for i in range(9) if v[i] == ' ']
    N = []
    for i in spots:
        N.append(v[:i] + ('O' if player == MIN else 'X',) + v[i + 1:])

    results = [minimax(w, MAX if player == MIN else MIN) for w in N]
    return max(results) if player == MAX else min(results)


def choose_move(v, player):
    spots = [i for i in range(9) if v[i] == ' ']
    N = []
    for i in spots:
        N.append(v[:i] + ('O' if player == MIN else 'X',) + v[i + 1:])

    results = [(minimax(w, MAX if player == MIN else MIN), spots[N.index(w)]) for w in N]
    print(sorted(results, key=lambda x: x[1]))
    return max(results)[1] if player == MAX else min(results)[1]


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
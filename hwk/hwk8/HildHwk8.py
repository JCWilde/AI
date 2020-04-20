from tkinter import *
from random import random


def perceptron_test(points, w1=random(), w2=random(), b=random()):
    r = .1
    for x, y, v in points:
        out = 1 if (w1 * x) + (w2 * y) + b > 0 else 0
        delta = v - out
        w1 += x * delta * r
        w2 += y * delta * r
        b = delta * r
    return w1, w2, b


def perceptron(points, w1, w2, b):
    for x, y in points:
        out = 1 if (w1 * x) + (w2 * y) + b > 0 else 0
        canvas.create_oval(15 * x + 300 - 5, -15 * y + 300 - 5,
                           15 * x + 300 + 10 - 5, -15 * y + 300 + 10 - 5,
                           fill=('black', 'white')[out])


def get_test_points(domain):
    str_tuple = (line.split() for line in open(domain))
    return ((float(l[0]), float(l[1]), int(l[2])) for l in str_tuple)


def get_points(domain):
    str_tuple = (line.split() for line in open(domain))
    return ((float(l[0]), float(l[1])) for l in str_tuple)


root = Tk()
canvas = Canvas(width=600, height=600, bg='white')
canvas.grid()

test_points = get_test_points('point_training.txt')
w1, w2, b = perceptron_test(test_points)

for _ in range(10000):
    w1, w2, b = perceptron_test(test_points, w1, w2, b)

points = get_points('new_data.txt')
perceptron(points, w1, w2, b)

# test line
canvas.create_line(0,  (2.405*-20+7.493)*-15+300,
                   600,  (2.405*20+7.493)*-15+300,
                   width=3, fill='red')

mainloop()

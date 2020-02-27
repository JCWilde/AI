# States in this puzzle are represented by tuples indicating where in each
# row the queen is.  For instance, (1,3,1,0) has a queen in row 0, col 1;
# row 1, col 3; row 2, col 1; and row 3, col 0;

from random import choice, random, randint, sample
from math import exp


def genetic(pop_size, h):
    # generate random popoulation
    pop = [tuple(randint(0,7) for i in range(8))
                              for j in range(pop_size)]    
    ticket_nums = [10, 10, 9, 8, 7, 6, 5, 4, 3, 2] + [1]*20  # max heuristic = 28
    while True:
        new_pop = []
        drawing = []

        #Z = sorted([h(c) for c in pop])
        #print(sum(Z), min(Z), max(Z))

        # give good heuristic individuals a higher chance reproducing        
        for p in pop:
            drawing += [p]*ticket_nums[h(p)] 
        
        for i in range(len(pop)):
            # mate x and y
            x, y = sample(drawing, 2)
            crossover = randint(1,6)
            child = x[:crossover] + y[crossover:]

            # random mutation
            if randint(0,99) < 20:
                loc = randint(0, 7)
                value = randint(0, 7)
                child = child[:loc] + (value,) + child[loc+1:]
                if h(child) == 0:
                    return child
            new_pop.append(child)
        pop = new_pop
                
        
        

# Generate all the neighbors, which we get by moving one queen at a time to
# any other location in its row.
def get_neighbors(t):
    N = []
    for i in range(len(t)):
        for j in range(len(t)):
            if j != t[i]:
                N.append(t[:i] + (j,) + t[i+1:])
    return N

# Calculates the number of pairs of queens that can attack each other.  The
# number of vertical pairs come from duplicates in the tuple. The number of
# diagonal pairs come from scanning below to the left and to the right of
# each queen.

def num_attacking(t):
    vertical = len(t) - len(set(t)) # number of duplications

    coords = list(enumerate(t))
    diagonal = 0
    
    for r in range(len(t)-1):
        c = t[r]
        rc = c + 1 
        lc = c - 1
        for nr in range(r+1, len(t)):
            if (nr, rc) in coords or (nr, lc) in coords:
                diagonal += 1
            rc += 1
            lc -= 1
    return vertical + diagonal

# nicely displays a tuple as the 2d representation of the board it represents.
def display(t):
    for x in t:
        for i in range(len(t)):
            if i == x:
                print('Q ', end=' ')
            else:
                print('. ', end=' ')
        print()

            
# Test things out.
t = (0,)*8
#ans = hill_climb(t, num_attacking)
#ans = anneal(t, num_attacking)
#ans = beam(t, num_attacking, 3)

ans = genetic(100, num_attacking)


print(ans)
print()
display(ans)


from itertools import combinations

def bfs_no_graph_path(start, goal):
    waiting = [start]
    parent = {start:None}
    while len(waiting) > 0:
        w = waiting.pop(0)
     
        for x in get_children(w):
            if x == goal:
                path = [x]
                x = w
                while parent[x] != None:
                    path.append(x)
                    x = parent[x]
                path.append(x)
                path.reverse()
                return path
            
            if x not in parent:
                parent[x] = w
                waiting.append(x)
    return []

def count_letters(s):
    return sum(1 for x in s if x.isalpha())

def count_digits(s):
    return sum(1 for x in s if x.isdigit())

def get_children(w):
    children = []
    left, right, boat = w
    if boat == 'L':    
        for x in left:        
            new_left = left.replace(x, '')
            new_right = ''.join(sorted(right + x))
            if (count_digits(new_left) >= count_letters(new_left) or count_digits(new_left) == 0) and (count_digits(new_right) >= count_letters(new_right) or count_digits(new_right) == 0):
                children.append((new_left, new_right, 'R'))
        for x, y in combinations(left, 2):
            new_left = left.replace(x, '').replace(y, '')
            new_right = ''.join(sorted(right + x + y))
            if (count_digits(new_left) >= count_letters(new_left) or count_digits(new_left) == 0) and (count_digits(new_right) >= count_letters(new_right) or count_digits(new_right) == 0):
                children.append((new_left, new_right, 'R'))
    if boat == 'R':
        for x in right:        
            new_right = right.replace(x, '')
            new_left = ''.join(sorted(left + x))
            if (count_digits(new_left) >= count_letters(new_left) or count_digits(new_left) == 0) and (count_digits(new_right) >= count_letters(new_right) or count_digits(new_right) == 0):
                children.append((new_left, new_right, 'L'))
        for x, y in combinations(right, 2):
            new_right = right.replace(x, '').replace(y, '')
            new_left = ''.join(sorted(left + x + y))
            if (count_digits(new_left) >= count_letters(new_left) or count_digits(new_left) == 0) and (count_digits(new_right) >= count_letters(new_right) or count_digits(new_right) == 0):
                children.append((new_left, new_right, 'L'))
    return children

i = 0
for x in bfs_no_graph_path(('123ABC','','L'),('','123ABC','R')):
    l,r,b = x
    l = l.replace('A','C').replace('B','C')
    l = l.replace('1','M').replace('2','M').replace('3','M')
    r = r.replace('A','C').replace('B','C')
    r = r.replace('1','M').replace('2','M').replace('3','M')
    print('{}. {}{}{}'.format(i,l,('<-','->')[b == 'R'],r))
    i += 1

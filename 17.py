import copy

debug = False

def adj(map, w, h, r, c):
    num_trees = 0
    num_lumber = 0
    for i in range(max(0, r-1), min(h, r+2)):
        for j in range(max(0, c-1), min(w, c+2)):
            if (i == r) and (j == c):
                continue
            else:
                if (map[i][j] == '|'):
                    num_trees += 1
                elif (map[i][j] == '#'):
                    num_lumber += 1
    return (num_trees, num_lumber)

def transition(map, w, h, r, c):
    (num_trees, num_lumber) = adj(map, w, h, r, c)
    if (map[r][c] == '.'):
        if (num_trees >= 3):
            return '|'
        else:
            return '.'
    if (map[r][c] == '|'):
        if (num_lumber >= 3):
            return '#'
        else:
            return '|'
    if (map[r][c] == '#'):
        if (num_trees >= 1) and (num_lumber >= 1):
            return '#'
        else:
            return '.'

def print_map(map):
    printing = ''
    for r in map:
        printing += ''.join(r) + '\n'
    return printing

def turns(num_turns, map):
    width = len(map[0])
    height = len(map)
    if (debug):
        print("Initial State")
        print(print_map(map))
    for i in range(num_turns):
        new_map = copy.deepcopy(map)
        for r in range(height):
            for c in range(width):
                new_map[r][c] = transition(map, width, height, r, c)
        map = new_map
        if (debug):
            print("Turn", i+1)
            print(print_map(map))
        num_trees = 0
        num_lumber = 0    
        for r in range(height):
            for c in range(width):
                if (map[r][c] == '|'):
                    num_trees += 1
                elif (map[r][c] == '#'):
                    num_lumber += 1
        print(i, num_trees, num_lumber, num_trees*num_lumber)
    num_trees = 0
    num_lumber = 0
    for r in range(height):
        for c in range(width):
            if (map[r][c] == '|'):
                num_trees += 1
            elif (map[r][c] == '#'):
                num_lumber += 1
    print(num_trees, num_lumber, num_trees*num_lumber)
    return num_trees*num_lumber

map = []
with open('17input1.txt') as ifile:
    for line in ifile:
        line = list(line.strip())
        map.append(line)
turns(1000000000, map)

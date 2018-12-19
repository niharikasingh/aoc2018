import copy

def find_occurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def print_map(map, moving):
    print_this_map = copy.deepcopy(map)
    for loc in moving:
        print_this_map[loc[0]][loc[1]] = loc[2]
    to_print = ''
    for line in print_this_map:
        to_print += ''.join(line)
        to_print += '\n'
    to_print += '\n\n'
    return to_print

# read input
map = []
carts = ['^', 'v', '<', '>']
dirs = ['|', '|', '-', '-']
turns = [
    ['<', '^', '>'],
    ['>', 'v', '<'],
    ['v', '<', '^'],
    ['^', '>', 'v']
]
moving = []
with open('13input1.txt') as ifile:
    lineno = 0
    cartno = 0
    for line in ifile:
        line = list(line[:-1])
        for c in range(len(carts)):
            found_carts = find_occurrences(line, carts[c])
            for f in found_carts:
                moving.append((lineno, f, carts[c], cartno))
                line[f] = dirs[c]
                cartno += 1
        map.append(line)
        lineno += 1
turns_id = [0] * cartno
# print(print_map(map, moving))

height = len(map)
width = len(map[0])
crash = False
ticks = 0
while (not crash):
    new_moving = []
    moving_iter = [(e[0], e[1]) for e in moving]
    for loc in moving:
        this_cart = loc[2]
        this_cart_id = carts.index(this_cart)
        this_cart_uid = loc[3]
        # print(moving_iter)
        if ((loc[0], loc[1]) in moving_iter):
            moving_iter.remove((loc[0], loc[1]))
            # move to next location
            if (this_cart_id == 0): # moving up
                next_pos = map[loc[0]-1][loc[1]]
                # print("up", (loc[0]-1, loc[1]))
                if ((loc[0]-1, loc[1]) in moving_iter):
                    # crash = True
                    moving_iter.remove((loc[0]-1, loc[1]))
                    for e in new_moving:
                        if (e[0] == loc[0]-1) and (e[1] == loc[1]):
                            new_moving.remove(e)
                            break
                    # print((loc[0]-1, loc[1]))
                else:
                    moving_iter.append((loc[0]-1, loc[1]))
                    if (next_pos == '/'):
                        new_moving.append((loc[0]-1, loc[1], '>', this_cart_uid))
                    elif (next_pos == '\\'):
                        new_moving.append((loc[0]-1, loc[1], '<', this_cart_uid))
                    elif (next_pos == '|'):
                        new_moving.append((loc[0]-1, loc[1], '^', this_cart_uid))
                    if (next_pos == '+'):
                        new_moving.append((loc[0]-1, loc[1], turns[this_cart_id][turns_id[this_cart_uid]], this_cart_uid))
                        turns_id[this_cart_uid] += 1
                        turns_id[this_cart_uid] %= 3
            elif (this_cart_id == 1): # moving down
                next_pos = map[loc[0]+1][loc[1]]
                # print("down", (loc[0]+1, loc[1]))
                if ((loc[0]+1, loc[1]) in moving_iter):
                    # crash = True
                    moving_iter.remove((loc[0]+1, loc[1]))
                    for e in new_moving:
                        if (e[0] == loc[0]+1) and (e[1] == loc[1]):
                            new_moving.remove(e)
                            break
                    # print((loc[0]+1, loc[1]))
                else:
                    moving_iter.append((loc[0]+1, loc[1]))
                    if (next_pos == '/'):
                        new_moving.append((loc[0]+1, loc[1], '<', this_cart_uid))
                    elif (next_pos == '\\'):
                        new_moving.append((loc[0]+1, loc[1], '>', this_cart_uid))
                    elif (next_pos == '|'):
                        new_moving.append((loc[0]+1, loc[1], 'v', this_cart_uid))
                    if (next_pos == '+'):
                        new_moving.append((loc[0]+1, loc[1], turns[this_cart_id][turns_id[this_cart_uid]], this_cart_uid))
                        turns_id[this_cart_uid] += 1
                        turns_id[this_cart_uid] %= 3
            elif (this_cart_id == 2): # moving left
                next_pos = map[loc[0]][loc[1]-1]
                # print("left", (loc[0], loc[1]-1))
                if ((loc[0], loc[1]-1) in moving_iter):
                    # crash = True
                    moving_iter.remove((loc[0], loc[1]-1))
                    for e in new_moving:
                        if (e[0] == loc[0]) and (e[1] == loc[1]-1):
                            new_moving.remove(e)
                            break
                    # print((loc[0], loc[1]-1))
                else:
                    moving_iter.append((loc[0], loc[1]-1))
                    if (next_pos == '/'):
                        new_moving.append((loc[0], loc[1]-1, 'v', this_cart_uid))
                    elif (next_pos == '\\'):
                        new_moving.append((loc[0], loc[1]-1, '^', this_cart_uid))
                    elif (next_pos == '-'):
                        new_moving.append((loc[0], loc[1]-1, '<', this_cart_uid))
                    if (next_pos == '+'):
                        new_moving.append((loc[0], loc[1]-1, turns[this_cart_id][turns_id[this_cart_uid]], this_cart_uid))
                        turns_id[this_cart_uid] += 1
                        turns_id[this_cart_uid] %= 3
            elif (this_cart_id == 3): # moving right
                next_pos = map[loc[0]][loc[1]+1]
                # print("right", (loc[0], loc[1]+1))
                if ((loc[0], loc[1]+1) in moving_iter):
                    # crash = True
                    moving_iter.remove((loc[0], loc[1]+1))
                    for e in new_moving:
                        if (e[0] == loc[0]) and (e[1] == loc[1]+1):
                            new_moving.remove(e)
                            break
                    # print((loc[0], loc[1]+1))
                else:
                    moving_iter.append((loc[0], loc[1]+1))
                    if (next_pos == '/'):
                        new_moving.append((loc[0], loc[1]+1, '^', this_cart_uid))
                    elif (next_pos == '\\'):
                        new_moving.append((loc[0], loc[1]+1, 'v', this_cart_uid))
                    elif (next_pos == '-'):
                        new_moving.append((loc[0], loc[1]+1, '>', this_cart_uid))
                    if (next_pos == '+'):
                        new_moving.append((loc[0], loc[1]+1, turns[this_cart_id][turns_id[this_cart_uid]], this_cart_uid))
                        turns_id[this_cart_uid] += 1
                        turns_id[this_cart_uid] %= 3
    # if (len(moving) != len(new_moving)):
    #     crash = True
    #     print(moving)
    #     print(new_moving)
    moving = sorted(new_moving)
    if (len(moving) == 1):
        print(moving)
        crash = True
    ticks += 1
    # print(moving)
    # print(print_map(map, moving))
print(ticks)
# 0,100 and 100,0 wrong

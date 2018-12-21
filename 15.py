import copy, math

debug = True

def turn(map):
    new_map = copy.deepcopy(map)
    width = len(map[0])
    height = len(map)
    for ri in range(height):
        for ci in range(width):
            # turns are based on starting positions
            this_cell = map[ri][ci]
            if (len(this_cell) > 1):
                looking_for = ''
                if (this_cell[0] == 'G'):
                    looking_for = 'E'
                else:
                    looking_for = 'G'
                target_found = False
                target = (-1, -1)
                distance_to_target = math.inf
                # find target cell
                for tri in range(height):
                    for tci in range(width):
                        test_cell = new_map[tri][tci]
                        # am i adjacent to enemy?
                        if (len(test_cell) > 1) and (test_cell[0] == looking_for):
                            if (abs(tri - ti) + abs(tci - ci) == 1):
                                target = (tri, tci)
                                target_found = True
                                break
                        # is this a cell adjacent to the enemy?
                        elif ((looking_for == 'E') and (test_cell == '<')) or ((looking_for == 'G') and (test_cell == '>')):
                            # check if reachable
                            reachableY1 = True
                            reachableY2 = True
                            for step in range(min(ri + 1, tri), max(ri, tri)):
                                if new_map[step][tci] not in ['.', '<', '>']:
                                    reachable = False
                                    break
                            for step in range(min(ci + 1, tci), max(ci, tci)):
                                if new_map[ri][step] not in ['.', '<', '>']:
                                    reachable = False
                                    break
                            if (reachable):
                                distance_to_this_target = abs(ri - tri) + abs(ci - tci)
                                # is this the nearest?
                                if (distance_to_this_target <= distance_to_target):
                                    distance_to_target = distance_to_this_target
                                    # is this the closest in reading order?
                                    if (tri < target[0]):
                                        target = (tri, tci)
                                    elif (tri == target[0]) and (tci < target[1]):
                                        target = (tri, tci)
                    if (target_found):
                        break
                # move
                if (target != (-1, -1)):
                    replace_with = ''
                    if (looking_for == 'E'):
                        replace_with = '<'
                    else:
                        replace_with = '>'
                    new_cell_loc = (-1, -1)
                    old_cell_loc = (ri, ci)
                    if (target[0] != ri):
                        if (target[0] < ri):
                            new_cell_loc = (ri-1, ci)
                        else:
                            new_cell_loc = (ri+1, ci)
                    elif (target[1] != ci):
                        if (target[1] < ci):
                            new_cell_loc = (ri, ci-1)
                        else:
                            new_cell_loc = (ri, ci-1)
                    new_map[new_cell_loc[0]][new_cell_loc[1]] = this_cell
                    if ()
                # attack
                if (target_found) or (distance_to_target == 2):
                    target_cell = new_map[target[0]][target[1]]
                    target_cell[1] -= 3
    # check if combat over
    saw_G = False
    saw_E = False
    for r in new_map:
        for c in r:
            if (len(c) > 1):
                if (c[0] == 'G'):
                    saw_G = True
                if (c[0] == 'E'):
                    saw_E = True
        if (sawG and sawE):
            break
    combat_over = not (sawG and sawE)
    return (new_map, combat_over)

def print_map(map):
    line_map = ''
    line_hps = ''
    for r in map:
        line_map = ''.join(r) + '   '
        line_hps = ''
        for c in r:
            if (len(c) > 1):
                line_hps += c[0] + '(' + c[1] + ') '
        print(line_map + line_hps)
    print('\n\n')

def game(ifilename):
    map = []
    with open(ifilename) as ifile:
        for line in ifile:
            temp_list = list(line.strip())
            for i in range(len(temp_list)):
                if (temp_list[i] == 'G') or (temp_list[i] == 'E'):
                    temp_list[i] = (temp_list[i], 200)
            map.append(temp_list)
    combat_over = False
    turns = 0
    while (not combat_over):
        (map, combat_over) = turn(map)
        if (not combat_over):
            turns += 1
        if (debug):
            print("Turn: ", turns)
            print_map(map)
    sum_hp = 0
    for r in map:
        for c in r:
            if (len(c) > 1):
                sum_hp += c[1]
    print("Turns:", turns, "Sum:", sum_hp, "Outcome:", turns * sum_hp)
    return turns * sum_hp

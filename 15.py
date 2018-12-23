import copy, collections, pdb

debug = True

def bfs(map, start_cell, w, h, looking_for):
    check_map = [[True]*w for i in range(h)]
    current_nodes = collections.deque([[start_cell]])
    found_nodes = []
    while (len(found_nodes) == 0) and (len(current_nodes) > 0):
        temp_index = len(current_nodes)
        for i in range(temp_index):
            curr_path = current_nodes.popleft()
            last_node_on_path = curr_path[-1]
            # print("Checking with node:", last_node_on_path)
            # if (last_node_on_path == (1, 4)):
            #     pdb.set_trace()
            # check in reading order
            if (last_node_on_path[0] > 0) and (check_map[last_node_on_path[0]-1][last_node_on_path[1]]) and (map[last_node_on_path[0]-1][last_node_on_path[1]][0] in ['.', looking_for]):
                # print("Got top")
                new_path = curr_path + [(last_node_on_path[0]-1, last_node_on_path[1])]
                current_nodes.append(new_path)
                if (map[last_node_on_path[0]-1][last_node_on_path[1]][0] == looking_for):
                    found_nodes.append(new_path)
            if (last_node_on_path[1] > 0) and (check_map[last_node_on_path[0]][last_node_on_path[1]-1]) and (map[last_node_on_path[0]][last_node_on_path[1]-1][0] in ['.', looking_for]):
                # print("Got left")
                new_path = curr_path + [(last_node_on_path[0], last_node_on_path[1]-1)]
                current_nodes.append(new_path)
                if (map[last_node_on_path[0]][last_node_on_path[1]-1][0] == looking_for):
                    found_nodes.append(new_path)
            if (last_node_on_path[1] < w-1) and (check_map[last_node_on_path[0]][last_node_on_path[1]+1]) and (map[last_node_on_path[0]][last_node_on_path[1]+1][0] in ['.', looking_for]):
                # print("Got right")
                new_path = curr_path + [(last_node_on_path[0], last_node_on_path[1]+1)]
                current_nodes.append(new_path)
                if (map[last_node_on_path[0]][last_node_on_path[1]+1][0] == looking_for):
                    found_nodes.append(new_path)
            if (last_node_on_path[0] < h-1) and (check_map[last_node_on_path[0]+1][last_node_on_path[1]]) and (map[last_node_on_path[0]+1][last_node_on_path[1]][0] in ['.', looking_for]):
                # print("Got bottom")
                new_path = curr_path + [(last_node_on_path[0]+1, last_node_on_path[1])]
                current_nodes.append(new_path)
                if (map[last_node_on_path[0]+1][last_node_on_path[1]][0] == looking_for):
                    found_nodes.append(new_path)
            check_map[last_node_on_path[0]][last_node_on_path[1]] = False
        # print("Current nodes:", current_nodes)
    # print("Found_nodes", found_nodes)
    if (len(found_nodes) == 0):
        return (False, 0, False)
    else:
        found_nodes.sort(key=lambda x: x[-2])
        found_nodes = [e for e in found_nodes if e[-2] == found_nodes[0][-2]]
        found_nodes.sort(key=lambda x: x[1])
        if (len(found_nodes[0]) == 2): # adjacent
            return (False, 0, True)
        elif (len(found_nodes[0]) == 3): # adjacent after moving
            return (True, found_nodes[0][1], True)
        return (True, found_nodes[0][1], False)

def find_target(map, start_cell, w, h, looking_for):
    # print(start_cell)
    lowest_hp = 201
    lowest_locations = []
    if (start_cell[0] > 0) and (map[start_cell[0]-1][start_cell[1]][0] == looking_for):
        if (map[start_cell[0]-1][start_cell[1]][1] == lowest_hp):
            lowest_locations.append((start_cell[0]-1, start_cell[1]))
        elif (map[start_cell[0]-1][start_cell[1]][1] < lowest_hp):
            lowest_hp = map[start_cell[0]-1][start_cell[1]][1]
            lowest_locations = [(start_cell[0]-1, start_cell[1])]
    if (start_cell[0] < h-1) and (map[start_cell[0]+1][start_cell[1]][0] == looking_for):
        if (map[start_cell[0]+1][start_cell[1]][1] == lowest_hp):
            lowest_locations.append((start_cell[0]+1, start_cell[1]))
        elif (map[start_cell[0]+1][start_cell[1]][1] < lowest_hp):
            lowest_hp = map[start_cell[0]+1][start_cell[1]][1]
            lowest_locations = [(start_cell[0]+1, start_cell[1])]
    if (start_cell[1] > 0) and (map[start_cell[0]][start_cell[1]-1][0] == looking_for):
        if (map[start_cell[0]][start_cell[1]-1][1] == lowest_hp):
            lowest_locations.append((start_cell[0], start_cell[1]-1))
        elif (map[start_cell[0]][start_cell[1]-1][1] < lowest_hp):
            lowest_hp = map[start_cell[0]][start_cell[1]-1][1]
            lowest_locations = [(start_cell[0], start_cell[1]-1)]
    if (start_cell[1] < w-1) and (map[start_cell[0]][start_cell[1]+1][0] == looking_for):
        if (map[start_cell[0]][start_cell[1]+1][1] == lowest_hp):
            lowest_locations.append((start_cell[0], start_cell[1]+1))
        elif (map[start_cell[0]][start_cell[1]+1][1] < lowest_hp):
            lowest_hp = map[start_cell[0]][start_cell[1]+1][1]
            lowest_locations = [(start_cell[0], start_cell[1]+1)]
    lowest_locations.sort()
    if (len(lowest_locations) == 0):
        return []
    return lowest_locations[0]

def turn(map, moved_last_turn, killed_last_turn, points):
    new_map = copy.deepcopy(map)
    width = len(map[0])
    height = len(map)
    completed_turn = False
    moved_this_turn = False
    killed_this_turn = False
    killed_elf = False

    for ri in range(height):
        for ci in range(width):
            # turns are based on starting positions
            this_cell = map[ri][ci]
            if (len(this_cell) > 1):
                # print(ri, ci)
                looking_for = ''
                subtract_points = 0
                if (this_cell[0] == 'G'):
                    looking_for = 'E'
                    subtract_points = 3
                else:
                    looking_for = 'G'
                    subtract_points = points
                # find closest target
                if (moved_last_turn or killed_last_turn or killed_this_turn):
                    (can_move, next_move, can_attack) = bfs(new_map, (ri, ci), width, height, looking_for)
                else:
                    # print("not doing bfs", moved_last_turn, killed_last_turn)
                    (can_move, next_move, can_attack) = (False, 0, True)
                # move
                if (can_move):
                    new_map[ri][ci] = '.'
                    new_map[next_move[0]][next_move[1]] = this_cell
                    moved_this_turn = True
                # attack
                if (can_attack):
                    if (can_move):
                        target = find_target(new_map, (next_move[0], next_move[1]), width, height, looking_for)
                    else:
                        target = find_target(new_map, (ri, ci), width, height, looking_for)
                    if (len(target) > 0):
                        target_cell = new_map[target[0]][target[1]]
                        if (target_cell[1] <= subtract_points):
                            if (target_cell[0] == 'E'):
                                killed_elf = True
                            new_map[target[0]][target[1]] = '.'
                            map[target[0]][target[1]] = '.'
                            killed_this_turn = True
                        else:
                            new_map[target[0]][target[1]] = (target_cell[0], target_cell[1]-subtract_points)
                    else:
                        can_attack = False
                completed_turn = (can_move or can_attack)
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
        if (saw_G and saw_E):
            break
    combat_over = not (saw_G and saw_E)
    return (new_map, combat_over, completed_turn, moved_this_turn, killed_this_turn, killed_elf)

def print_map(map):
    line_map = ''
    line_hps = ''
    for r in map:
        line_map = ''
        line_hps = '   '
        for c in r:
            if (len(c) > 1):
                line_map += c[0]
                line_hps += c[0] + '(' + str(c[1]) + ') '
            else:
                line_map += c
        print(line_map + line_hps)
    print('\n\n')

def game(ifilename):
    print(ifilename)
    orig_map = []
    with open(ifilename) as ifile:
        for line in ifile:
            temp_list = list(line.strip())
            for i in range(len(temp_list)):
                if (temp_list[i] == 'G') or (temp_list[i] == 'E'):
                    temp_list[i] = (temp_list[i], 200)
            orig_map.append(temp_list)
    points = 3
    elf_killed = True
    while (elf_killed):
        elf_killed = False
        combat_over = False
        turns = 0
        moved_this_turn = True
        killed_this_turn = False
        points += 1
        map = copy.deepcopy(orig_map)
        while (not combat_over):
            (map, combat_over, completed_turn, moved_this_turn, killed_this_turn, elf_killed) = turn(map, moved_this_turn, killed_this_turn, points)
            if (elf_killed):
                combat_over = True
            if (not combat_over) or (combat_over and completed_turn):
                turns += 1
            if (debug):
                print("Turn: ", turns)
                # print_map(map)
        print("Points:", points, " Elf killed:", elf_killed, " Turns:", turns)
    sum_hp = 0
    for r in map:
        for c in r:
            if (len(c) > 1):
                sum_hp += c[1]
    print("Points:", points, "Turns:", turns, "Sum:", sum_hp, "Outcome:", turns * sum_hp)
    return turns * sum_hp

# assert game('15input3.txt') == 36334
# assert game('15input2.txt') == 27730
# assert game('15input4.txt') == 39514
# assert game('15input5.txt') == 27755
# assert game('15input6.txt') == 28944
# assert game('15input7.txt') == 18740
assert game('15input2.txt') == 4988
assert game('15input4.txt') == 31284
assert game('15input5.txt') == 3478
assert game('15input6.txt') == 6474
assert game('15input7.txt') == 1140
game('15input1.txt')

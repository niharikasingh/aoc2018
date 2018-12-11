import math

width_board = 0
height_board = 0
points = {}
with open('6input1.txt', 'r') as ifile:
    for line in ifile:
        line = line.strip().split(', ')
        w = int(line[0])
        h = int(line[1])
        points[(w, h)] = []
        if (w > width_board):
            width_board = w
        if (h > height_board):
            height_board = h

def manhattan(p0, p1):
    x_dist = abs(p0[0] - p1[0])
    y_dist = abs(p0[1] - p1[1])
    if (p0[0] == 0) or (p0[0] == width_board) or (p1[0] == 0) or (p1[0] == width_board) or (p0[1] == 0) or (p0[1] == height_board) or (p1[1] == 0) or (p1[1] == height_board):
        inf_dist = math.inf
    else:
        inf_dist = 0
    return (x_dist + y_dist, inf_dist)

def display(points, width_board, height_board):
    board = [['.'] * (width_board + 1) for i in range(height_board + 1)]
    i = 0
    for p_main in points:
        board[p_main[1]][p_main[0]] = chr(ord('A') + i)
        for p_assoc in points[p_main]:
            if (p_assoc != math.inf):
                board[p_assoc[1]][p_assoc[0]] = chr(ord('a') + i)
        i += 1
    return board

region = 0
for i in range(width_board + 1):
    for j in range(height_board + 1):
        # if ((i, j) in points):
        #     continue
        # min_dist = (math.inf, 0)
        # min_point = (-1, -1)
        # tie = False
        # for p in points:
        #     this_dist = manhattan(p, (i, j))
        #     # print("from", i, j, "to", p, "is", this_dist)
        #     if (this_dist[0] < min_dist[0]):
        #         min_dist = this_dist
        #         min_point = p
        #         tie = False
        #     elif (this_dist[0] == min_dist[0]): # ties go to no one
        #         tie = True
        # if (not tie):
        #     points[min_point].append((i,j))
        #     if (min_dist[1] == math.inf) and (math.inf not in points[min_point]):
        #         points[min_point].append(math.inf)
        total_dist = 0
        for p in points:
            total_dist += manhattan((i, j), p)[0]
        if (total_dist < 10000):
            region += 1

# display_board = display(points, width_board, height_board)
# for db in display_board:
#     print(db)
# for p in points:
#     if (math.inf not in points[p]):
#         print(p, len(points[p]) + 1)
print(region)

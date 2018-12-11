import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
with open('7input1.txt', 'r') as ifile:
    for line in ifile:
        start_node = line[5]
        end_node = line[36]
        G.add_edge(start_node, end_node)

to_visit = []
for node in G:
    if (G.in_degree(node) == 0):
        to_visit.append(node)

to_visit.sort()
visited = []
DELAY_CONST = 60
workers = [[0, 0] for i in range(5)]
timer = 0
while (len(to_visit) > 0):
    # curr_visit = to_visit[0]
    # del to_visit[0]
    #
    # prereqs_complete = True
    # prereqs = list(G.predecessors(curr_visit))
    # for p in prereqs:
    #     if (p not in visited):
    #         prereqs_complete = False
    #         break
    #
    # if (curr_visit not in visited) and (prereqs_complete):
    #     visited.append(curr_visit)
    #     to_visit.extend(list(G.successors(curr_visit)))
    #     to_visit.sort()
    for w in workers:
        if (w[0] == 0):
            if (w[1] != 0) and (w[1] not in visited):
                # complete old job
                visited.append(w[1])
    for w in workers:
        if (w[0] == 0):
            # start new job
            i = 0
            while (i < len(to_visit)):
                curr_visit = to_visit[i]
                if (curr_visit in visited):
                    del to_visit[i]
                    i += 1
                elif (curr_visit in [j[1] for j in workers]):
                    del to_visit[i]
                    i += 1
                else:
                    prereqs_complete = True
                    prereqs = list(G.predecessors(curr_visit))
                    for p in prereqs:
                        if (p not in visited):
                            prereqs_complete = False
                            break
                    if (prereqs_complete == False):
                        i += 1
                    else:
                        w[1] = curr_visit
                        w[0] = DELAY_CONST + 1 + (ord(curr_visit) - ord('A'))
                        del to_visit[i]
                        to_visit.extend(list(G.successors(w[1])))
                        to_visit.sort()
                        i = len(to_visit)
        w[0] = max(0, w[0] - 1)
    timer += 1
    print(workers)

workers.sort(key=lambda tup: tup[0])
temp_timer = 0
for w in workers:
    if (w[0] != 0):
        visited.append(w[1])
        timer += (w[0] - temp_timer)
        temp_timer += w[0]
print(''.join(visited))
print(timer)
# nx.draw(G, with_labels=True)
# plt.show()
# OFSWAP wrong
# 932 wrong

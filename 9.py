from collections import deque

def get_winner(p, m):
    ms = deque()
    ps = [0] * p
    for i in range(m+1):
        if ((i != 0) and (i % 23 == 0)):
            cp = i % p
            ps[cp] += i
            ms.rotate(7)
            remove_marble = ms.pop()
            # print("Saw 23")
            # print(remove_marble)
            ps[cp] += remove_marble
            ms.rotate(-1)
            # print(ms[-1])
        else:
            ms.rotate(-1)
            ms.append(i)
    ws = max(ps)
    print(ws)
    return ps.index(ws)

with open('9input1.txt', 'r') as ifile:
    for line in ifile:
        line = line.strip().split(' ')
        num_players = int(line[0])
        num_marbles = int(line[1])
        correct_ans = int(line[2])
        print(num_players, num_marbles, correct_ans)
        print(get_winner(num_players, num_marbles))

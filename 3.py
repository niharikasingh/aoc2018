import re

pattern = re.compile(r'(?P<id>\d*) @ (?P<left>\d*),(?P<top>\d*): (?P<width>\d*)x(?P<height>\d*)')
fabric = [[False for i in range(1000)] for j in range(1000)]
fabricoverlap = [[False for i in range(1000)] for j in range(1000)]
answer = 0

with open('3input1.txt', 'r') as ifile:
    for line in ifile:
        match = pattern.search(line.strip())
        top = int(match.group('top'))
        left = int(match.group('left'))
        height = int(match.group('height'))
        width = int(match.group('width'))
        for i in range(top, top+height):
            for j in range(left, left+width):
                if (fabric[i][j]):
                    fabricoverlap[i][j] = True
                else:
                    fabric[i][j] = True

with open('3input1.txt', 'r') as ifile:
    for line in ifile:
        match = pattern.search(line.strip())
        id = int(match.group('id'))
        top = int(match.group('top'))
        left = int(match.group('left'))
        height = int(match.group('height'))
        width = int(match.group('width'))
        hasoverlapped = False
        for i in range(top, top+height):
            for j in range(left, left+width):
                if (fabricoverlap[i][j]):
                    hasoverlapped = True
                    break
            if (hasoverlapped):
                break
        if (not hasoverlapped):
            print(id)

answer = sum([sum(row) for row in fabricoverlap])
print(answer)

import math

data = []
with open('10input1.txt', 'r') as ifile:
    for line in ifile:
        line = line.strip().split(', ')
        line = [int(i) for i in line]
        data.append(line)

# find min bounding box
# minarea = []
# for i in range(0, 20000):
#     minx = math.inf
#     miny = math.inf
#     maxx = 0
#     maxy = 0
#     for p in data:
#         newpx = p[0] + i*p[2]
#         newpy = p[1] + i*p[3]
#         if (newpx < minx):
#             minx = newpx
#         if (newpx > maxx):
#             maxx = newpx
#         if (newpy < miny):
#             miny = newpy
#         if (newpy > maxy):
#             maxy = newpy
#     thisarea = (maxx - minx) * (maxy - miny)
#     print(i, minx, maxx, miny, maxy)
#     minarea.append(thisarea)

mintime = 10144 # minarea.index(min(minarea))
print(mintime)

drawing = [['.'] * 65 for i in range(10)]
for p in data:
    px = p[0] + mintime*p[2] - 116
    py = p[1] + mintime*p[3] - 140
    drawing[py][px] = '#'
for d in drawing:
    print(''.join(d))

# import sys
# sys.setrecursionlimit(10000) # 10000 is an example, try with different values
from collections import deque

with open('8input1.txt', 'r') as ifile:
    numbers = ifile.read().strip().split(' ')
numbers = [int(i) for i in numbers]

children = deque()
children2 = deque()
metadata = deque()
values = deque()
def int_parse(a):
    # s = 0
    i = 0
    while (i < len(a)):
        # leaf node
        if (a[i] == 0):
            # s += sum(a[i+2 : i+2+a[i+1]])
            values.append(sum(a[i+2 : i+2+a[i+1]]))
            print("Leaf node:", a[i:i+2+a[i+1]], sum(a[i+2 : i+2+a[i+1]]))
            i += 2 + a[i+1]
            c = children.pop()
            c -= 1
            children.append(c)
        else:
            # metadata
            if ((len(children) > 0) and (children[-1] == 0)):
                children.pop()
                c2 = children2.pop()
                m_len = metadata.pop()
                # s += sum(a[i : i+m_len])
                temp_arr = []
                temp_sum = 0
                print(values)
                for j in range(c2):
                    temp_arr = [values.pop()] + temp_arr
                print(temp_arr)
                for j in a[i:i+m_len]:
                    if (j-1 < len(temp_arr)):
                        temp_sum += temp_arr[j-1]
                values.append(temp_sum)
                print("Adding parent metadata:", a[i:i+m_len], temp_sum)
                i += m_len
                if (len(children) > 0):
                    c = children.pop()
                    c -= 1
                    children.append(c)
            # node
            else:
                children.append(a[i])
                children2.append(a[i])
                metadata.append(a[i+1])
                print("Parent node:", a[i], a[i+1])
                i += 2
    # print(s)
    print(values.pop())
int_parse(numbers)

# def rec_parse(a):
#     if (len(a) == 0):
#         return (0, 0)
#     # print("Iteration with", a)
#     # base case just add up all metadata
#     elif (a[0] == 0):
#         s = sum(a[2:2+a[1]])
#         l = 2 + a[1]
#         # print("Base case", a[0:2+a[1]], l, s)
#         return (l, s)
#     else:
#         num_child = a[0]
#         l = 2
#         s = 0
#         for i in range(num_child):
#             (l1, s1) = rec_parse(a[l:])
#             l += l1
#             s += s1
#         s += sum(a[l:l+a[1]])
#         # print("Cont case", a[0:2], a[l:l+a[1]], l, s)
#         return (l, s)
#
# print(rec_parse(numbers))
# 19713 wrong

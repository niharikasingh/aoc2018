# from collections import Counter
#
# count2 = 0
# count3 = 0
# with open('2input1.txt', 'r') as ifile:
#     for line in ifile:
#         temp_values = Counter(list(line.strip())).values()
#         if (2 in temp_values):
#             count2 += 1
#         if (3 in temp_values):
#             count3 += 1
# print(count2*count3)
#
# from collections import OrderedDict
# from pprint import pprint

# mydict = {}
# with open('2input2.txt', 'r') as ifile:
#     for line in ifile:
#         line = line.strip()
#         sline = ''.join(sorted(line))
#         if (sline in mydict):
#             mydict[sline].append(line)
#         else:
#             mydict[sline] = [line]
#
# omydict = OrderedDict(sorted(mydict.items(), key=lambda t: t[0]))
# pprint(dict(omydict.items()))
# keys_omydict = list(omydict.keys())
# for i in range(len(keys_omydict) - 1):
#     first_key_array = omydict[keys_omydict[i]]
#     second_key_array = omydict[keys_omydict[i + 1]]
#     for first_key in first_key_array:
#         for second_key in second_key_array:
#             differences = 0
#             for i1 in range(len(first_key)):
#                 if first_key[i1] != second_key[i1]:
#                     differences += 1
#                 if (differences > 1):
#                     break
#             if (differences == 1):
#                 print(first_key, second_key)
#                 break

myarr = []
with open('2input1.txt', 'r') as ifile:
    for line in ifile:
        line = line.strip()
        myarr.append(line)

for i in range(len(myarr)):
    for j in range(i, len(myarr)):
        first_key = myarr[i]
        second_key = myarr[j]
        differences = 0
        for k in range(len(first_key)):
            if first_key[k] != second_key[k]:
                differences += 1
            if (differences > 1):
                break
        if (differences == 1):
            print(first_key)
            print(second_key)
            break
    if (differences == 1):
        break

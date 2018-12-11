from dateutil.parser import parse
import re

pattern = re.compile(r'\[(?P<date>.*)\].{1,7}#?(?P<id>\d*) (?P<desc>.*)')
input = []
with open('4input1.txt', 'r') as ifile:
    for line in ifile:
        match = pattern.search(line.strip())
        date = parse(match.group('date'))
        desc = match.group('desc')
        if (desc == 'begins shift'):
            desc = int(match.group('id'))
        input.append((date, desc))
sorted_input = sorted(input, key=lambda tup: tup[0])

checker = {}
id = 0
checked = False
for i in range(len(sorted_input)):
    desc = sorted_input[i][1]
    if (isinstance(desc, int)):
        if (desc not in checker):
            checker[desc] = [0] * 60
        id = desc
    elif (not checked):
        asleep_minute = sorted_input[i][0].minute
        up_minute = sorted_input[i+1][0].minute
        checked = True
        for j in range(asleep_minute, up_minute):
            checker[id][j] += 1
    elif (checked):
        checked = False

max_guard_id = -1
max_minute = -1
max_sum = -1
for guard in checker:
    # if (sum(checker[guard]) > max_sum):
    #     max_sum = sum(checker[guard])
    #     max_guard_id = guard
    #     max_minute = checker[guard].index(max(checker[guard]))
    if (max(checker[guard]) > max_sum):
        max_sum = max(checker[guard])
        max_guard_id = guard
        max_minute = checker[guard].index(max(checker[guard]))
print(max_guard_id, max_minute)
print(max_guard_id * max_minute)

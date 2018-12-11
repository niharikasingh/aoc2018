from ast import literal_eval

answer = 0
notFoundDuplicate = True
seen = set([])
while (notFoundDuplicate):
    with open('1input1.txt', 'r') as ifile:
        for line in ifile:
            answer += literal_eval(line.strip())
            if (answer not in seen):
                seen.add(answer)
            else:
                notFoundDuplicate = False
                break
print(answer)

import re

text = ''
with open('5input1.txt', 'r') as ifile:
    text = ifile.read().strip()

def find_length(text):
    text = list(text)
    t0 = ''
    t1 = ''
    restart = True
    while (restart):
        restart = False
        loop = len(text) - 1
        i = 0
        # print(text)
        while (i < loop):
            # print(i)
            t0 = text[i]
            t1 = text[i+1]
            if (t0 != t1) and (t0.upper() == t1.upper()):
                restart = True
                # print("removing", t0, t1)
                del text[i]
                del text[i]
                loop -= 2
                i -= 1
            else:
                i += 1
    # print(''.join(text))
    return len(text)

current_min = len(text)
for a in list('abcdefghijklmnopqrstuvwxyz'):
    to_remove = a + a.upper()
    new_text = re.sub('[' + to_remove + ']', '', text)
    # print("removing:", to_remove, "result:", new_text)
    new_min_to_test = find_length(new_text)
    # print(a, new_min_to_test)
    current_min = min(current_min, new_min_to_test)
print(current_min)

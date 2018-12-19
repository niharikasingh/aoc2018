transitions = {}
num_generations = 1000

def convert(c):
    if (c == '#'):
        return '1'
    else:
        return '0'

def deconv(a):
    answer = ''
    for i in range(len(a)):
        if (a[i] == '1'):
            answer += '#'
        else:
            answer += '.'
    return(answer)

def find_sum(state):
    answer = 0
    for i in range(len(state)):
        if (state[i] == '1'):
            answer += (i - (num_generations * 2))
    print(answer)
    return answer

# process input
with open('12input1.txt') as ifile:
    for line in ifile:
        if ('initial') in line:
            line = line.strip()[15:]
            state = ['0'] * (num_generations * 2)
            for i in range(len(line)):
                state += [convert(line[i])]
            state += ['0'] * (num_generations * 2)
            # print("creating", state)
        else:
            line = line.strip()
            if (len(line) > 1):
                line = line.split(' => ')
                transition_state = ''
                for i in range(5):
                    transition_state += convert(line[0][i])
                transitions[int(transition_state,2)] = convert(line[1])
# print(transitions)
# print(deconv(state[18:]))
prev_sum = find_sum(state)
for i in range(num_generations):
    next_state_total = ['0'] * len(state)
    # print('creating again', next_state_total)
    for j in range(2,len(state)-3):
        this_state = ''.join(state[j-2:j+3])
        if (int(this_state,2) in transitions):
            next_state = transitions[int(this_state,2)]
        else:
            next_state = '0'
        next_state_total[j] = next_state
    state = next_state_total
    new_sum = find_sum(state)
    print(new_sum - prev_sum)
    prev_sum = new_sum
    # print(deconv(state[18:]))

# after finding convergence (+45 per iteration), answer for part 2 is: 
# ((50000000000 - 1000) * 45) + 45120

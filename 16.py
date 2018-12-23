from operator import and_

def addr(before, instruction, after):
    regA_value = before[instruction[1]]
    regB_value = before[instruction[2]]
    regC_index = instruction[3]
    if (after[regC_index] == regA_value + regB_value):
        print("addr")
        return 1
    return 0

def addi(before, instruction, after):
    regA_value = before[instruction[1]]
    B_value = instruction[2]
    regC_index = instruction[3]
    if (after[regC_index] == regA_value + B_value):
        print("addi")
        return 1
    return 0

def mulr(before, instruction, after):
    regA_value = before[instruction[1]]
    regB_value = before[instruction[2]]
    regC_index = instruction[3]
    if (after[regC_index] == regA_value * regB_value):
        print("mulr")
        return 1
    return 0

def muli(before, instruction, after):
    regA_value = before[instruction[1]]
    B_value = instruction[2]
    regC_index = instruction[3]
    if (after[regC_index] == regA_value * B_value):
        print("muli")
        return 1
    return 0

def banr(before, instruction, after):
    regA_value = before[instruction[1]]
    regB_value = before[instruction[2]]
    regC_index = instruction[3]
    if (after[regC_index] == regA_value & regB_value):
        print("banr")
        return 1
    return 0

def bani(before, instruction, after):
    regA_value = before[instruction[1]]
    B_value = instruction[2]
    regC_index = instruction[3]
    if (after[regC_index] == regA_value & B_value):
        print("bani")
        return 1
    return 0

def borr(before, instruction, after):
    regA_value = before[instruction[1]]
    regB_value = before[instruction[2]]
    regC_index = instruction[3]
    if (after[regC_index] == regA_value | regB_value):
        print("borr")
        return 1
    return 0

def bori(before, instruction, after):
    regA_value = before[instruction[1]]
    B_value = instruction[2]
    regC_index = instruction[3]
    if (after[regC_index] == regA_value | B_value):
        print("bori")
        return 1
    return 0

def setr(before, instruction, after):
    regA_value = before[instruction[1]]
    regC_index = instruction[3]
    if (after[regC_index] == regA_value):
        print("setr")
        return 1
    return 0

def seti(before, instruction, after):
    A_value = instruction[1]
    regC_index = instruction[3]
    if (after[regC_index] == A_value):
        print("seti")
        return 1
    return 0

def gtir(before, instruction, after):
    A_value = instruction[1]
    regB_value = before[instruction[2]]
    regC_index = instruction[3]
    if (after[regC_index] == int(A_value > regB_value)):
        print("gtir")
        return 1
    return 0

def gtri(before, instruction, after):
    regA_value = before[instruction[1]]
    B_value = instruction[2]
    regC_index = instruction[3]
    if (after[regC_index] == int(regA_value > B_value)):
        print("gtri")
        return 1
    return 0

def gtrr(before, instruction, after):
    regA_value = before[instruction[1]]
    regB_value = before[instruction[2]]
    regC_index = instruction[3]
    if (after[regC_index] == int(regA_value > regB_value)):
        print("gtrr")
        return 1
    return 0

def eqir(before, instruction, after):
    A_value = instruction[1]
    regB_value = before[instruction[2]]
    regC_index = instruction[3]
    if (after[regC_index] == int(A_value == regB_value)):
        print("eqir")
        return 1
    return 0

def eqri(before, instruction, after):
    regA_value = before[instruction[1]]
    B_value = instruction[2]
    regC_index = instruction[3]
    if (after[regC_index] == int(regA_value == B_value)):
        print("eqri")
        return 1
    return 0

def eqrr(before, instruction, after):
    regA_value = before[instruction[1]]
    regB_value = before[instruction[2]]
    regC_index = instruction[3]
    if (after[regC_index] == int(regA_value == regB_value)):
        print("eqrr")
        return 1
    return 0

with open('16input1.txt') as ifile:
    all_lines = []
    for line in ifile:
        line = line.strip().split(',')
        line = [int(e) for e in line]
        all_lines.append(line)
# answer = 0
answer = [[1]*16 for i in range(16)]
for line in all_lines:
    b = line[0:4]
    i = line[4:8]
    a = line[8:12]
    temp_answer = [addr(b, i, a), addi(b, i, a), mulr(b, i, a), muli(b, i, a), banr(b, i, a), bani(b, i, a), borr(b, i, a), bori(b, i, a), setr(b, i, a), seti(b, i, a), gtir(b, i, a), gtri(b, i, a), gtrr(b, i, a), eqir(b, i, a), eqri(b, i, a), eqrr(b, i, a)]
    operator = i[0]
    answer[operator] = list(map(and_, answer[operator], temp_answer))
for o in answer:
    print(sum(o), '\t', o)

# mapping functions
def send_to_function(opcode, b, i, a):
    if (opcode == 0):
        bori(b, i, a)
    elif (opcode == 1):
        muli(b, i, a)
    elif (opcode == 2):
        banr(b, i, a)
    elif (opcode == 3):
        bani(b, i, a)
    elif (opcode == 4):
        gtir(b, i, a)
    elif (opcode == 5):
        setr(b, i, a)
    elif (opcode == 6):
        addr(b, i, a)
    elif (opcode == 7):
        eqir(b, i, a)
    elif (opcode == 8):
        seti(b, i, a)
    elif (opcode == 9):
        addi(b, i, a)
    elif (opcode == 10):
        eqrr(b, i, a)
    elif (opcode == 11):
        eqri(b, i, a)
    elif (opcode == 12):
        borr(b, i, a)
    elif (opcode == 13):
        gtrr(b, i, a)
    elif (opcode == 14):
        mulr(b, i, a)
    elif (opcode == 15):
        gtri(b, i, a)

# 599 too low

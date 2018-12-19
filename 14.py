import copy

def next10(i):
    # start condition
    board = [3, 7]
    elves = [0, 1]
    found = False
    # while (len(board) < i + 10):
    while (not found):
        to_add = board[elves[0]] + board[elves[1]]
        if (to_add < 10):
            board.append(to_add)
            if (board[-1*len(i):] == i):
                found = len(board[:-1*len(i)])
        else:
            board.append(1)
            board.append(to_add%10)
            if (board[-1*len(i):] == i):
                found = len(board[:-1*len(i)])
            elif (board[-1*len(i)-1:-1] == i):
                found = len(board[:-1*len(i)-1])
        elves[0] = (elves[0] + board[elves[0]] + 1) % len(board)
        elves[1] = (elves[1] + board[elves[1]] + 1) % len(board)
        # print board
        # to_print = copy.deepcopy(board)
        # to_print[elves[0]] = "(" + str(to_print[elves[0]]) + ")"
        # to_print[elves[1]] = "[" + str(to_print[elves[1]]) + "]"
        # print(to_print)
    # print(board[i:i+10])
    # return board[i:i+10]
    print(found)
    return found

# assert next10(5) == [0,1,2,4,5,1,5,8,9,1]
# assert next10(9) == [5,1,5,8,9,1,6,7,7,9]
# assert next10(18) == [9,2,5,1,0,7,1,0,8,5]
# assert next10(2018) == [5,9,4,1,4,2,9,8,8,2]
# print(next10(760221))

assert next10([0,1,2,4,5]) == 5
assert next10([5,1,5,8,9]) == 9
assert next10([9,2,5,1,0]) == 18
assert next10([5,9,4,1,4]) == 2018
print(next10([7,6,0,2,2,1]))

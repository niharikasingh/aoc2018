def find_power(x, y, gsn):
    rack_id = x+10
    power_level = rack_id * y
    power_level += gsn
    power_level *= rack_id
    power_level = (power_level % 1000) // 100
    power_level -= 5
    return power_level

assert find_power(3, 5, 8) == 4
assert find_power(122, 79, 57) == -5
assert find_power(217, 196, 39) == 0
assert find_power(101, 153, 71) == 4

def create_grid(gsn):
    grid = [[0]*300 for i in range(300)]
    for y in range(300):
        for x in range(300):
            grid[y][x] = find_power(x + 1, y + 1, gsn)
            if (y > 0):
                grid[y][x] += grid[y-1][x]
            if (x > 0):
                grid[y][x] += grid[y][x-1]
            if (y > 0) and (x > 0):
                grid[y][x] -= grid[y-1][x-1]

    max_x = -1
    max_y = -1
    max_sum = -1
    max_size = -1
    for size in range(300):
        for y in range(300-size):
            for x in range(300-size):
                this_sum = grid[y][x] + grid[y+size][x+size] - grid[y+size][x] - grid[y][x+size]
                if (this_sum > max_sum):
                    max_sum = this_sum
                    max_x = x
                    max_y = y
                    max_size = size
    print(max_x+2, max_y+2, max_size+0)
    return(max_x+2, max_y+2, max_size+0)

assert create_grid(18) == (90,269,16)
assert create_grid(42) == (232,251,12)
create_grid(3463)

# ADVENT OF CODE 2021 - DAY2

data = open("data.txt", 'r')
move_list = list()

for line in data:
    m = line.replace("\n", "")
    move_list.append(m)


# part 1
def move_submarine(mv):
    horizontal_pos = 0
    depth = 0
    for move in mv:
        x = int(move[-1])
        if "forward" in move:
            horizontal_pos += x
        elif "down" in move:
            depth += x
        elif "up" in move:
            depth -= x
    return horizontal_pos * depth


# part 2
def move_submarine_complex(mv):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for move in mv:
        x = int(move[-1])
        if "forward" in move:
            horizontal_pos += x
            depth += (aim * x)
        elif "down" in move:
            aim += x
        elif "up" in move:
            aim -= x
    return horizontal_pos * depth


print(move_submarine(move_list))
print(move_submarine_complex(move_list))
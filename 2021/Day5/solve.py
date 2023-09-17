# ADVENT OF CODE 2021 - DAY5

import numpy as np

with open("data.txt", 'r') as f:
    lines = [entry.strip() for entry in f.readlines()]

cor_list = []
max_cor = 0
for line in lines:
    coordinates = tuple(line.split(" -> "))
    coordinates = [tuple(num.split(',')) for num in coordinates]
    coordinates = tuple((int(x), int(y)) for x, y in coordinates)
    if max(max(coordinates)) > max_cor:
        max_cor = max(max(coordinates))
    cor_list.append(coordinates)

diagram = np.zeros((max_cor+1, max_cor+1))


# part 1 (diagonal=False) and part 2 (diagonal=True)
def place_cords(cor_list, diagonal=False):
    for pair in cor_list:
        first, sec = pair
        x1, y1 = first
        x2, y2 = sec
        vent_line = []
        vent_cor = [0, 0]  # initializing by giving value of zeros
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                vent_cor[0] = x1
                vent_cor[1] = i
                vent_line.append(tuple(vent_cor))
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                vent_cor[1] = y1
                vent_cor[0] = i
                vent_line.append(tuple(vent_cor))
        # checking for diagonal
        elif diagonal:
            dis = abs(x1 - x2)
            # negative angle
            if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
                x, y = min(pair)
                for i in range(dis + 1):
                    vent_cor[0] = x + i
                    vent_cor[1] = y + i
                    vent_line.append(tuple(vent_cor))
            # positive angle
            elif (x1 > x2 and y1 < y2) or (x1 < x2 and y1 > y2):
                x = max(x1, x2)
                y = min(y1, y2)
                for i in range(dis + 1):
                    vent_cor[0] = x - i
                    vent_cor[1] = y + i
                    vent_line.append(tuple(vent_cor))
        # placing cors on diagram
        for cor in vent_line:
            x, y = cor
            diagram[y][x] += 1


def count_scores(diagram):
    counter = 0
    for i in range(max_cor + 1):
        for j in range(max_cor + 1):
            if diagram[i][j] >= 2:
                counter += 1
    return counter


place_cords(cor_list, True)
print(count_scores(diagram))

# ADVENT OF CODE 2021 - DAY4
# *** part1 with help of Jadi Mirmirani @ yt ***
from re import sub
import numpy as np


class Board:
    def __init__(self, data):
        self.data = data
        self.marked = np.zeros((5, 5))  # to keep track of marked nums

    def mark_num(self, num):
        for i in range(5):
            for j in range(5):
                if self.data[i][j] == num:
                    self.marked[i][j] = 1

    def check_win(self, called):
        # check every column
        for i in range(5):
            won = True
            for j in range(5):
                if self.marked[i, j] == 0:
                    won = False
            if won:
                return True
        # check every row
        for i in range(5):
            won = True
            for j in range(5):
                if self.marked[j, i] == 0:
                    won = False
            if won:
                return True
        return False

    def score(self):
        score = 0
        for i in range(5):
            for j in range(5):
                if self.marked[i][j] == 0:  # if it hasn't been marked
                    score += self.data[i][j]
        return score


with open("data.txt", 'r') as f:
    lines = [entry.strip() for entry in f.readlines()]


marked_nums = lines[0].split(',')
marked_nums = [int(n) for n in marked_nums]
boards = []

for i in range(100):  # we have 100 boards
    curr_board = np.zeros((5, 5))
    for j in range(5):  # each board
        curr_line = lines[(i*6)+(j+2)]
        curr_row = sub(' +', ' ', curr_line).split(' ')
        curr_board[j] = [int(n) for n in curr_row]
    boards.append(Board(curr_board))


# part 1
def first_win_score(marked_nums, boards):
    for m in marked_nums:
        for board in boards:
            board.mark_num(m)
            if board.check_win(m):
                return board.score()*m


# part 2
def last_win_score(marked_nums, boards):
    winners_pos = []
    last_winner_called = 0
    for m in marked_nums:
        for i in range(len(boards)):
            if i not in winners_pos:
                boards[i].mark_num(m)
                if boards[i].check_win(m):
                    winners_pos.append(i)
                    last_winner_called = m
    last_winner = boards[winners_pos[-1]]
    return last_winner.score()*last_winner_called


print(first_win_score(marked_nums, boards))
print(last_win_score(marked_nums, boards))


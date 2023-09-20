# ADVENT OF CODE 2021 - DAY6

from collections import Counter

with open("data.txt", 'r') as f:
    for line in f:
        timers = [int(x) for x in line.split(',')]


# part 1
def fish_counter(timers, days):
    for _ in range(1, days + 1):
        updated_timers = []
        timers_to_add = []
        for timer in timers:
            if timer == 0:
                timer = 6
                updated_timers.append(8)
            else:
                timer -= 1
            updated_timers.append(timer)
        timers = updated_timers
    total_fish = len(timers)
    return total_fish


# part 2
def fish_counter2(timers, days):
    # for more days we use a counter dictionary
    timers_counter = dict(Counter(timers))
    for _ in range(1, days + 1):
        # -1 is for fish that are about to reset
        for i in range(-1, 8):
            if timers_counter.get(i+1) is None:
                timers_counter[i] = 0
            else:
                timers_counter[i] = timers_counter.get(i+1)
        # creating new fish
        timers_counter[8] = timers_counter[-1]
        timers_counter[6] += timers_counter[-1]
        timers_counter[-1] = 0  # reset
    total_fish = sum(timers_counter.values())
    return total_fish


print(fish_counter(timers, 80))
print(fish_counter2(timers, 256))

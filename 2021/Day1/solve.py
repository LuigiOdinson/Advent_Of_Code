# ADVENT OF CODE 2021 - DAY1

data = open("data.txt", 'r')
depth_list = list()

for line in data:
    num = int(line.replace("\n", ""))
    depth_list.append(num)


# part 1
def depth_increases(dp):
    counter = 0
    for i in range(1, len(dp)):
        if dp[i] > dp[i - 1]:
            counter += 1
    return counter


# part 2
def sum_depth_increases(dp):
    counter = 0
    for i in range(len(dp)-3):
        a = dp[i] + dp[i+1] + dp[i+2]
        b = dp[i+1] + dp[i+2] + dp[i+3]
        if b > a:
            counter += 1
    return counter


print(depth_increases(depth_list))
print(sum_depth_increases(depth_list))

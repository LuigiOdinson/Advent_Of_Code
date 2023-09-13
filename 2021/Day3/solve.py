# ADVENT OF CODE 2021 - DAY3

num_list = list()
with open("data.txt", 'r') as data:
    for line in data:
        n = line.replace("\n", "")
        num_list.append(n)


# part 1
def power_consumption(nl):
    gamma_rate, epsilon_rate = str(), str()

    for pos in range(len(nl[0])):
        nums_at_pos = [int(num[pos]) for num in nl]
        if sum(nums_at_pos) > len(nl) // 2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    return gamma_rate * epsilon_rate


# part 2
def life_support_rating(nl):
    oxygen_gen_rating, co2_scrubber_rating = [], []
    # copying the nl on two lists
    for i in nl:
        oxygen_gen_rating.append(i)
        co2_scrubber_rating.append(i)
    common, least_common = int(), int()

    # oxygen_gen_rating
    for pos in range(len(nl[0])):
        if len(oxygen_gen_rating) == 1:
            break

        nums_at_pos = [num[pos] for num in oxygen_gen_rating]
        if nums_at_pos.count('1') >= len(oxygen_gen_rating) / 2:
            common = "1"
        else:
            common = "0"
        # filtering elements out
        oxygen_gen_rating = [num for num in oxygen_gen_rating
                             if num[pos] == common]

    # co2_scrubber_rating
    for pos in range(len(nl[0])):
        if len(co2_scrubber_rating) == 1:
            break

        nums_at_pos = [num[pos] for num in co2_scrubber_rating]
        if nums_at_pos.count('1') >= len(co2_scrubber_rating) / 2:
            least_common = "0"
        else:
            least_common = "1"
        co2_scrubber_rating = [num for num in co2_scrubber_rating
                               if num[pos] == least_common]

    oxygen_gen_rating = int(oxygen_gen_rating[0], 2)
    co2_scrubber_rating = int(co2_scrubber_rating[0], 2)
    return oxygen_gen_rating * co2_scrubber_rating


print(power_consumption(num_list))
print(life_support_rating(num_list))

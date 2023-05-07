import random

# generate list of 4 random elements (0 or 1)
random_list = [random.randint(0, 1) for x in range(4)]

# set the result based on the list values
if random_list == [0, 0, 0, 0]:
    result = "A"
elif random_list == [1, 1, 1, 1]:
    result = "B"
elif random_list == [1, 0, 0, 0]:
    result = "C"
    # subtract 1 from the sum for result C
    sum_ = sum(random_list) - 2
else:
    # calculate the sum of the list elements for all other cases
    sum_ = sum(random_list)
    result = str(sum_)

# print the result
if result == "C":
    print(f"The list is {random_list} and the result is {result} ({sum_}).")
else:
    print(f"The list is {random_list} and the result is {result}.")
# We want to generate all the numbers of three digits where:

# the sum of their digits is equal to 10
# their digits are in increasing order (the numbers may have two or more equal contiguous digits)
# The numbers that fulfill these constraints are: [118, 127, 136, 145, 226, 235, 244, 334]. There are 8 numbers in total with 118 being the lowest and 334 being the greatest.

# Task
# Implement a function which receives two arguments:

# the sum of digits (sum)
# the number of digits (count)
# This function should return three values:

# the total number of values which have count digits that add up to sum and are in increasing order
# the lowest such value
# the greatest such value
# Note: if there are no values which satisfy these constaints, you should return an empty value (refer to the examples to see what exactly is expected).

# Examples
# find_all(10, 3)  =>  [8, 118, 334]
# find_all(27, 3)  =>  [1, 999, 999]
# find_all(84, 4)  =>  []

from itertools import combinations_with_replacement

def find_all(sum_dig, digs):
    count = 0
    min_val = None
    max_val = None

    for comb in combinations_with_replacement(range(1, 10), digs):
        if sum(comb) == sum_dig:
            num = int(''.join(map(str, comb)))
            count += 1
            if min_val is None:
                min_val = num
            max_val = num

    return [count, min_val, max_val] if count else []
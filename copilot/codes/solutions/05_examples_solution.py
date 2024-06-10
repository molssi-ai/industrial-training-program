# 1. takes two arrays of integers as input
# 2. returns the sum of the two arrays

def sum_arrays(array1, array2):
    return sum(array1) + sum(array2)

print(sum_arrays([1, 2, 3], [4, 5, 6])) # 21

# write a function called sum_arrays_correct that:
# 1. takes two arrays of integers as input
# 2. returns the sum of the two arrays
# Example: sum_arrays_correct([1, 2, 3], [4, 5, 6]) => [5, 7, 9]

def sum_arrays_correct(array1, array2):
    return [array1[i] + array2[i] for i in range(len(array1))]

print(sum_arrays_correct([1, 2, 3], [4, 5, 6])) # [5, 7, 9]
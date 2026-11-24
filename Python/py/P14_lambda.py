square = lambda x : x**2

result = square(10)
print(result)

add = lambda x, y : x + y
print(add(15,2)) # 17

# add no. if no. is even else return 0
add_even = lambda x, y : x + y if x % 2 == 0 and y % 2 == 0 else 0
print(add_even(3,6)) # 0
print(add_even(2,6)) # 8

# filter
nums = [1,2,3,4,5,6,7,8,9]

even_num = filter(lambda x : x % 2 == 0, nums)       # <filter object at 0x000001BF431420E0>
even_num = list(filter(lambda x : x % 2 == 0, nums)) # [2, 4, 6, 8]

print(even_num)

# map
square_num = map(lambda x: x ** 2, nums) # <map object at 0x0000015A12AEBD80>
square_num = list(map(lambda x: x ** 2, nums)) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

nums2 = [10,20,30,40,50,60,70,80,90]
even_nums = list(map(lambda x, y : x + y, nums, nums2)) # [11, 22, 33, 44, 55, 66, 77, 88, 99]
print(even_nums)

# reduce
from functools import reduce
total_sum = reduce(lambda x, y : x + y, nums) # 45
print(total_sum)
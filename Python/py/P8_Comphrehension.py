# list comprehension

num = [x for x in range(1,21)]  # list of numbers from 1 to 20
print(num)

even_num = [x for x in range(1,21) if x % 2 == 0] # list of even numbers from 1 to 20
print(even_num)

# list of even numbers from 1 to 20 if the number is not even then make the number as zero
even_num_zeros = [x if x % 2 == 0 else x*0 for x in range(1,21)]
print(even_num_zeros)

# nested list comprehension
nested_list = [[1,2,3],[4,5,6],[7,1,4]]
nums_list = [num for nums in nested_list for num in nums]
print(nums_list)
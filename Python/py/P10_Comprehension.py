# dictionary comprehension

nums = [10,9,30,7,50,6,100]

square = {x : x**2 for x in nums} # key of num and square-root of number
print(square)

# key of num and square-root of number if the number is even
even_square_num = {x : x**2 for x in nums if x % 2 == 0} 
print(even_square_num)

# key of num and square-root of number if the number is even else make the value 0
even_square_zeros = {x : x**2 if x % 2 == 0 else x*0 for x in nums} 
print(even_square_zeros)
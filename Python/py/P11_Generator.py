# generator
def generate_nums(n):
    i = 1
    while i <= n:
        yield i
        i += 1

values = generate_nums(5)

print(values) # <generator object generate_nums at 0x0000016906E09560>

print(next(values)) # 1
print(next(values)) # 2
print(next(values)) # 3
print(next(values)) # 4

for value in values:
    print(value)        # 1, 2, 3, 4, 5


# generator comprehension
square_num = (x**2 for x in range(1,11))

for square in square_num:
    print(square)
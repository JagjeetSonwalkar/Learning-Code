# create a genertor function which uses 3 yields keyword and iterate on these value
def python_generator():
    yield 0
    yield 1
    yield 2

for x in python_generator():
    print(x) 
# output: 0 1 2

# create a generrator function to give sequence of value
def python_generator(n):
    count = 0
    while count < n:
        yield count
        count += 1

for x in python_generator(5):
    print(x)
# output: 0 1 2 3 4

# Generator comprehension
square_num = (x**2 for x in range(1,11)) # 

print(square_num) # <generator object <genexpr> at 0x000002178EAE9560>
for square in square_num:
    print(square)

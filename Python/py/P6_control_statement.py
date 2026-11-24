# print 10 to 0

# break
for i in range(10, 0, -1):
    if i == 5:
        break
    print(i, end=", ")
print()

# continue
for i in range(10, 0, -1):
    if i == 5:
        continue
    print(i, end=", ")
print()

# pass
chars = ['a', 'b', 'c']

for char in chars:
    pass

def function():
    pass

class Demo:
    pass
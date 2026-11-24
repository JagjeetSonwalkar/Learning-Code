# use of iter() & next() - using ietartor

name = "Rohit45"

iterator_value = iter(name)

print(iterator_value) # <str_ascii_iterator object at 0x00000280349B1AE0>

print(next(iterator_value)) # R
print(next(iterator_value)) # o
print(next(iterator_value)) # h
print(next(iterator_value)) # i
print(next(iterator_value)) # t
print(next(iterator_value)) # 4
print(next(iterator_value)) # 5
# print(next(iterator_value)) # ERROR : StopIteration

fruits = ["Mango", "Apple", "banana", "orange"]
iter_value = iter(fruits)       # Iterating through an iterator

print(iter_value) # <list_iterator object at 0x00000138942B05B0>
print(next(iter_value)) # Mango
print(next(iter_value)) # Apple
print(next(iter_value)) # banana
print(next(iter_value)) # orange

print(fruits == iter_value) # False
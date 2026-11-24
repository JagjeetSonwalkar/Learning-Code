# calculate of mod of number by 2 using custome iterator

class CustomIterator:
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.value = 0
        return self
    
    def __next__(self):
        if self.value <= self.max:
            result = self.value % 2
            self.value += 1
            return result
        else:
            raise StopIteration
# end of class

num_object = CustomIterator(3)

iter_num_object = iter(num_object)

print(iter_num_object)                      # <__main__.CustomIterator object at 0x000001F577EFC6E0>
print("(mod 0 % 2)",next(iter_num_object))  # (mod 0 % 2) 0
print("(mod 1 % 2)",next(iter_num_object))  # (mod 1 % 2) 1
print("(mod 2 % 2)",next(iter_num_object))  # (mod 2 % 2) 0
print("(mod 3 % 2)",next(iter_num_object))  # (mod 3 % 2) 1
# print("(mod 4 % 2)",next(iter_num_object)) # EXECPTION - StopIteration
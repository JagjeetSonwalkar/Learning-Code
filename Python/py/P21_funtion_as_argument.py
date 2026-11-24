# pass function as arguments
def incerment(value):
    return value + 1

def decrement(value):
    return value - 1

def operate(fun_argument, number):
    result = fun_argument(number)
    return result

if __name__ == "__main__":
    ret = operate(incerment, 5)
    print(ret)

    ret = operate(decrement, 5)
    print(ret)

# return a function as value
def outer_fun():
    def inner_fun():
        return "hello my friend!"
    return inner_fun

if __name__ == "__main__":
    new = outer_fun()
    print(new)      # <function outer_fun.<locals>.inner_fun at 0x00000228951E7690>
    print(new())    # hello my friend!
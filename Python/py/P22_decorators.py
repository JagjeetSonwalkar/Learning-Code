def smart_divide(func):
    def inner(a,b):
        print("I am going to divide")
        if b == 0:
            return "Cannot divide"
        return func(a, b)
    return inner

@smart_divide
def div(a, b):
    return a/b

if __name__ == "__main__":
    ret = div(10,5)
    print(ret)
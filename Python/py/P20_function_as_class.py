# function as class
def info(name):
    print("my name is:",name)

if __name__ == "__main__":
    info("rohit")

    # info_obj = info() # ERROR
    info_obj = info
    info_obj("Virat")

# nested functions

def fun_outer(x):
    def fun_inner(y):
        return x + y
    return fun_inner

add_five_obj = fun_outer(5) # <function fun_outer.<locals>.fun_inner at 0x000001F2B4087690>
result = add_five_obj(6)    # 11
print(add_five_obj)
print(result)
# function arguments

# position argument
def info(name, age):
    print("Your name:",name)
    print("Your age:", age)

info("Rohit", 45)
info(18, "Virat") # ERROR - WRONG WAY 

# keyword argument
info(name="Rohit", age="45")
info(age = 18, name="virat")
info("Rohit", age = 249)
info(age = 15, "WRONG_MAN") # ERROR - WRONG WAY 

def info(name = "X", age = 18):
    print("Your name:",name)
    print("Your age:", age)

info()
info(name = "King")
info(age = 20)
info("Hardik", 44)

def info(**kwargs):
    print("Player info: ")
    for i in kwargs:
        print(i,': ',kwargs[i])

info(name="Rohit", J_no=45, score = 249, ipl="MI")

def total_score(*runs):
    score = 0
    for i in runs:
        score += i
    return score

ret = total_score(1,45,18,44,65,6,1,9,8,0)
ret = total_score(1,45,18)
print("TOTAL SCORE:",ret)
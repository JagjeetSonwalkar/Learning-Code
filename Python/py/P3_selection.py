age  = int(input("Enter your age: "))

# only for if
if age > 18 and age <= 59:
    print("You can drive the car.")
elif age == 18:
    print("You can drive the car from next year!")
elif age >= 60:
    print("Do you have renewed licence (yes-no)")
    license_str = input().lower()
    if license_str == "no":
        print("you cant drive the Car")
    else:
        print("You can drive the car.")
else:
    print("You can't Drive the car!")

# one line if else
num1 = 11
num2 = 11
print(num1) if num2 > num1 else print('Equal') if num1 == num2 else print(num2)


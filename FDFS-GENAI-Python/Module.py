from Functions import *

print("Choose your operations: addition,Subraction,division,Muliplication,floordiv")

choice = input("Enter your choice: ")

num1 = float(input("Enter the values: "))
num2 = float(input("Enter the values: "))

if choice.lower() == "addition":
    print(add(num1,num2))

elif choice.lower() == "subraction":
    print(sub(num1,num2))

elif choice.lower() == "division":
    print(div(num1,num2))

elif choice.lower() == "Multiplication":
    print(mul(num1,num2))

elif choice.lower() == "floordiv":
    print(floor(num1,num2))

else:
    print("Please enter the correct choice")
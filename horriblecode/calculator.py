#function that takes both inputed numbers and returns their sum
def add(num1, num2):
    return num1 + num2

#function that takes both inputed numbers and returns their divided result
def divide(num1, num2):
    return num1 / num2

#function that takes both inputed numbers and returns their product sum
def multiply(num1, num2):
    return num1 * num2

#taking user inputs for variables
num1 = int(input("Please insert first number: "))
num2 = int(input("Please insert second number: "))
select = int(input("Would you like to add, divide or multiply your numbers? \n1: add\n2: divide\n3: multiply\n"))

if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif select == 2:
    print(num1, "/", num2, "=", divide(num1, num2))
elif select == 3:
    print(num1, "X", num2, "=", multiply(num1, num2))
else:
    print("Not an option")



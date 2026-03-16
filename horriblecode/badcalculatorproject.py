dnumber = 0
anumber = 0
mnumber = 0
snumber = 0

def add(firstnumber, secondnumber):
    anumber = firstnumber + secondnumber
    return anumber

def divide(firstnumber, secondnumber):
    dnumber = firstnumber / secondnumber
    return dnumber

def multiply(firstnumber, secondnumber):
    mnumber = firstnumber * secondnumber
    return mnumber
    


firstnumber = int(input("Please insert first number: "))
secondnumber = int(input("Please insert second number: "))
selectedchoice = int(input("Would you like to add, divide or multiply your numbers? \n1: add\n2: divide\n3: multiply\n"))

if selectedchoice == 1:
    selectedchoiceagain = int(input("So you would like to add ", firstnumber, " and ", secondnumber, " ? yes =1, no =2"))
    if selectedchoiceagain == "y":
        anumber = add(firstnumber, secondnumber)
        print(firstnumber, "+", secondnumber, "=", add(firstnumber, secondnumber))
elif selectedchoice == 2:
    selectedchoiceagain = int(input("So you would like to divide ", firstnumber, " and ", secondnumber, " ? yes =1, no =2"))
    if selectedchoiceagain == "y":
        dnumber = divide(firstnumber, secondnumber)
        print(firstnumber, "/", secondnumber, "=", divide(firstnumber, secondnumber))
elif selectedchoice == 3:
    selectedchoiceagain = int(input("So you would like to multiply ", firstnumber, " and ", secondnumber, " ? yes =1, no =2"))
    if selectedchoiceagain == "y":
        mnumber = multiply(firstnumber, secondnumber)
        print(firstnumber, "X", secondnumber, "=", multiply(firstnumber, secondnumber))




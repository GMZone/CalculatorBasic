def addition(x, y):  # Addition function
    return x+y


def subtraction(x, y):  # Subtraction function
    return x-y


def multiplication(x, y):  # Multiplication function
    return x*y


def division(x, y):  # Division function
    return x//y


def TakeInput_Int():
    while True:
        try:
            userin = int(input())
        except:
            userin = None
        if userin == None:
            print("Enter a valid number \n")
            continue
        else:
            return userin


def TakeInput_Str():
    while True:
        userin=input().lower()
        if userin=="add" or userin=="subtract" or userin=="multiply" or userin=="divide":
            return userin
        else:
            print("Enter valid input \n")
            continue

def GoAgain():
    userin=""
    while True:
        try:
            userin=input("Type a yes or no \n").lower()
        except:
            print("")   
        if userin=="yes" or userin=="no":
            return userin
        else:
            continue     

while True:
    print("Enter the first number")
    num1 = TakeInput_Int()
    print("Enter the second number")
    num2 = TakeInput_Int()
    print("Would you like to:-\n1. Add\n2.Subtract\n3.Multiply\n4.Divide\n\n")
    operation = TakeInput_Str()

    if operation=="add":
        print(addition(num1, num2))
    elif operation == "subtract":
        print(subtraction(num1, num2))
    elif operation == "multiply":
        print(multiplication(num1, num2))
    elif operation == "divide":
        print(division(num1, num2))

    print("Do you want to calculate again?\n")
    goagain_decision=GoAgain()

    if goagain_decision=="yes":
        continue
    elif goagain_decision=="no":
        break

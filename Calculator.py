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
            continue
        else:
            return userin


def TakeInput_Str():
    while True:
        userin = input()
        if userin == "":
            continue
        else:
            if userin == "add" or userin == "subtract" or userin =="multiply" or userin == "divide":
                break
            else:
                continue

while True:
    print("Enter the first number")
    num1 = TakeInput_Int()
    print("Enter the second number")
    num2 = TakeInput_Int()
    print("Would you like to:-\n1. Add\n2.Subtract\n3.Multiply\n4.Divide\n\n")
    operation = TakeInput_Str()

    print(operation)

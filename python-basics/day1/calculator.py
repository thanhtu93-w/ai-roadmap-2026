while True:
    print("Calculator(Press e and enter to exit)")
    if input() == "e":
        break
    num1= int(input("Enter first number : "))
    operator = input("Enter operator : ")
    num2= int(input("Enter second number : "))
    if num1%2==0:
        print("First number is even")
    else:
        print("First number is odd")
    if num2%2==0:
        print("Second number is even")
    else:
        print("Second number is odd")
    if operator == "+":
        print("Result:",num1+num2)
    elif operator == "-":
        print("Result:",num1-num2)
    elif operator == "*":
        print("Result:",num1*num2)
    elif operator == "/":
        if num2==0:
            print("Can not divide by zero")
        else:
            print("Result:",num1/num2)
    else:
        print("Invalid operator")
    
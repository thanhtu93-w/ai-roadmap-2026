try:
    print ("x divide y :")
    x = int(input("Please enter x: "))
    y = int(input("Please enter y: "))
    print ("Output:",x/y)
except ZeroDivisionError:
    print( "Can not divide by zero")
except ValueError:
    print("Value Incorrect ")
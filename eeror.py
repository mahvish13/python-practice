try:
    numerator=float(input("Enter first the value:"))
    denominator=float(input("Enter Second the value:"))
    result=numerator/denominator
    print(f"Result:(result)")
except ZeroDivisionError:
    print("Error can't devide by zero")
except ValueError:
    print("there is value error")
    





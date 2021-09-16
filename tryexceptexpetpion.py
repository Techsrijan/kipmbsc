try:
    print("Freeze open")
    a = int(input("Enter First number"))
    b = int(input("Enter second number"))
    d = a / b
    print("D=", d)


except ValueError:
    print("You have entered a character not a number")

except ZeroDivisionError:
    print("b cant be zero")

except Exception:
    print("somthing went wrong")

finally:
    print("freeze close")
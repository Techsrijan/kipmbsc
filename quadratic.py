from math import *
try:
    a=int(input("Enter First number"))
    b=int(input("Enter second number"))
    c=int(input("Enter Third number"))
    # nested if else
    d=b*b-4*a*c
    if d==0:
        print("roots are real and equal")
        x1=x2=-b/(2*a)
        print("X1=",x1,"x2=",x2)
    elif d>0:
        print("roots are real and unequal")
        x1=(-b+sqrt(d))/(2*a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print("X1=", x1, "x2=", x2)
    else:
        print("roots are imaginary")

except ValueError:
        print("You have entered a character not a number")

except ZeroDivisionError:
    print("b cant be zero")

except Exception:
    print("somthing went wrong")

finally:
    print("freeze close")
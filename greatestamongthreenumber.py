a=int(input("Enter First number"))
b=int(input("Enter second number"))
c=int(input("Enter Third number"))
# nested if else
if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatset")
elif b>c:
    print("b is greatest")
else:
    print("c is greatest")
year=int(input("Enter Year"))
if year%100==0:
    if year%400==0:
        print("Leap year=",year)
    else:
        print("Not Leap year=",year)
elif year%4==0:
    print("Leap year=",year)
else:
    print("Not Leap year=",year)
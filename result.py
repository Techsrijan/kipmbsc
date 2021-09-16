a=int(input("Enter Marks of hindi"))
b=int(input("Enter Marks of english"))
c=int(input("Enter Marks of computer"))
d=int(input("Enter Marks of math"))
e=int(input("Enter Marks of physics"))
total=a+b+c+d+e
print("total Marks=",total)

per=(total/500)*100
print("Percentage=",per)
if per<33:
    print("You are Fail")
elif per>=33 and per<45:
    print("Third division")
elif per>=45 and per<60:
    print("Second division")
elif per>=60:
    print("First division")


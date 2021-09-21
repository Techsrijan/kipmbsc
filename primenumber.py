n=int(input("Enter any number"))
a=2
while a<=n-1:
    if n%a==0:
        print("not prime no=",n)
        break
    a=a+1
else:
    print("prime no=",n)
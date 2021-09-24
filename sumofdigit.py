#n=int(input("Enter any number"))
num=100
while num<=999:
    n=num
    sum=0
    while n>0:
        a=n%10
        sum=sum+a
        n=n//10

    print(sum)
    num=num+1
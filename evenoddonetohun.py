n=1
s=0
m=1
while n<=10:
    if n % 2 == 0:
        print("even no=",n)
        s=s+n
        m=m*n
    n=n+1

print(s,m)
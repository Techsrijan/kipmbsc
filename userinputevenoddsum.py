n=int(input("enter starting number "))
e=int(input("enter ending  number "))
s=0
m=1
if n<e:
    while n<=e:
        if n % 2 == 0:
            print("even no=",n)
            s=s+n
            m=m*n
        n=n+1

    print(s,m)
else:
    s = 0
    m = 1
    if n > e:
        while n >= e:
            if n % 2 == 0:
                print("even no=", n)
                s = s + n
                m = m * n
            n = n - 1

        print(s, m)
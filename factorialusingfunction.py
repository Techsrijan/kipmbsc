def fact(n):
    f=1
    #for i in range(1,n+1):
    #    f=f*i
    for i in range(n,1,-1):
        print(i)
        f=f*i
    print(f)


fact(6)
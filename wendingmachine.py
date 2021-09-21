n=int(input("how many toffee u want"))
stock=15
k=1
while k<=n:
    if stock>=k:
        print("collect toffe=",k)

    else:
        print("Out Of stock")
        break
    k=k+1
else:  # when loop runs properly
    print("thanks Please visit again")
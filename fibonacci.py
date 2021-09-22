import time
f=0
s=1
print(f,"\t",s,end='')
i=1
while i<=8:
    time.sleep(1)
    t=f+s
    print("\t",t,end='')
    f=s
    s=t
    i=i+1

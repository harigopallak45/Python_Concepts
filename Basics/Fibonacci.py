p1=0
p2=1
n=int(input("Enter a num:"))
c=0
while c<n:
    print(p1)
    t=p1+p2
    p1=p2
    p2=t
    c+=1

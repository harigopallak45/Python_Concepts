n=int(input("enter a num"))
s=0
while n>0:
    temp = n%10
    s+=temp
    n//=10
    if s<=9 and n==0:
        print (s)
    elif n==0:
        n=s
        s=0

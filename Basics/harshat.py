n=int(input("enter a num"))
t=n
s=0
while n>0:
    temp = n%10
    s+=temp
    n//=10
if t%s==0:
    print("It is harsath num")
else :
    print ("it i not harsath num")

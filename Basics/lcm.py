n1=int(input("Enter a num"))
n2=int(input("Enter a num"))
i=1
t=0
while i<=n1 and i<=n2:
    if n1%i==0 and n2%i==0:
        t=i
    i+=1
lcm=(n1*n2)//t
print("LCM of the given nos is",lcm)

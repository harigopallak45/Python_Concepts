n1=int(input("N1 is:"))
n2=int(input("N2 is :"))
i=1
while i<=n1 and i<=n2:
    if n1%i==0 and n2%i==0:
        n=i
    i+=1
print("GCD of the given numbers is:",n)

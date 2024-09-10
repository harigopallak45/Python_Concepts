num = int(input("enter the num"))
l=0
while num>0:
    temp= num%10
    if l<temp:
        l=temp
    num//=10
print(l)

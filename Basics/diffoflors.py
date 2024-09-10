num = int(input("enter the num"))
s=l=num%10
while num>0:
    temp= num%10
    if l<temp:
        l=temp
    elif s>temp:
        s=temp
    num//=10
print("l",l,"s",s)
d=l-s
print("The Diff btn of the given num is :",d)

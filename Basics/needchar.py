st=input("Enter the String")
ch=input("Enter the Char")
i=c=0
while i<len(st):
    if st[i]==ch:
        c+=1
    i+=1
print(ch," is ",c,"times")

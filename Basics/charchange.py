st=input("Enter the String")
ch=input("Enter the Char")
ch1=input("Enter the Char to change")
s=''
i=0
while i<len(st):
    if st[i]==ch:
        s+=ch1
    else :
        s+=st[i]
    i+=1
print(s)

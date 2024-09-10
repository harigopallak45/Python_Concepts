s=input()
i=0
t=""
while i<len(s):
    if s[i]>='A' and s[i]<='Z' or s[i]>='a' and s[i]<='z' or s[i]>='0' and s[i]<='9':
        pass
    else:
        t+=s[i]
    i+=1
print(t)

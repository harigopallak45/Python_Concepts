num=int(input("print")) #fact is perfect ot not
p=i=1
while i<=num:     #why num / 2
    p*=i
    res=0
    j=1
    while (j<p):
        if p%j==0:
            res+=j
        j+=1
    print(i,num,res)
    if res==num:
        print("It is Perfect")
    else:
        print("Not Perfect")
    i+=1



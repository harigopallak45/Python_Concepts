num = int(input("enter the num"))
i=1
sum=0
while i<num:
    if num%i==0:
        sum+=i
    i+=1
if num<sum:
    print("it is abunded num")
else :
    print("it is not abunded num")

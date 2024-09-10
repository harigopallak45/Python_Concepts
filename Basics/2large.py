# WAP to print second largest element from the given without sorting
l=[1,4,6,2,5,6,9,8]
ld=0 
sld=0 
for i in l: 
    if i>ld: 
        sld=ld 
        ld=i 
    elif sld>ld and ld!=i:  
        sld=i 
print(sld)          

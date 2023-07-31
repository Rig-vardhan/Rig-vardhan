#   Q. print the third smallest and third largest from the array 

def sort(aa):
    z=0
    for xx in range(len(aa)-1):
        z+=1
        for x in range(0,len(aa)-z):
            if aa[x]>aa[x+1]:
                aa[x],aa[x+1]=aa[x+1],aa[x]
                
b=eval(input("Enter the arrya :"))

b=list(b)

sort(b)

a1=a2=x1=x2=0

for x in range(len(b)-1):
    if a1<2:
        if b[x]<b[x+1]:
            a1+=1
        if a1==2:
            x1=x+1
    if a2<2:
        if b[len(b)-x-1]>b[len(b)-x-2]:
            a2+=1
        if a2==2:
            x2=len(b)-x-2
    if a1==3 and a2==3:
        break
    
if a1<2 and a2<2:
    print('Neither third largest nor third smallest number present in this arrya')
else:
    if x1==x2:
        print("This number is third smallest and also third largest number ",b[x1])
    else:
        print("The third smallest number is ",b[x1],"\nThe third largest number is ",b[x2])

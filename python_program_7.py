

#   Q. print the sum of alternate elements seperately.

a=list(eval(input("Enter the arrya :")))
a1=a2=0
x1=x2=""

print("Output :-\n ")
for x in range(len(a)):
    if x%2==0:
        if x!=0:
            x1+='+'
        x1+=str(a[x])
        a1+=a[x]
    if x%2!=0:
        if x > 1:
            x2+='+'
        x2+=str(a[x])
        a2+=a[x]
        
print("Sum of odd elements of arrya ",x1,"=",a1)
print("Sum of even elements of arrya",x2,"=",a2)

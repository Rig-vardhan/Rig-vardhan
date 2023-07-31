# Find the element that is not smaller than its neighbors in arrya.

a=list(eval(input("Enter the Arrya :")))
b=str("")
print(', ,  Next Element ')
for x in range(len(a)-2):
    if a[x]<a[x+1] and a[x+1]>a[x+2]:
        print("Previous Element = ",a[x],"The Element = ",a[x+1],"Next Element = ",a[x+2])

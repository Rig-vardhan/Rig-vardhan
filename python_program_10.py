# Find the missing number between the range...
# from the smalest element of arrya till the bigest element of arrya.
def sort(aa):
    z=0
    for xx in range(len(aa)-1):
        z+=1
        for x in range(0,len(aa)-z):
            if aa[x]>aa[x+1]:
                aa[x],aa[x+1]=aa[x+1],aa[x]
a=list(eval(input("Enter the Arrya :")))
a=set(a)
a=list(a)
b=str("")
for x in range(len(a)-1):
    a1=a[x+1]-a[x]
    if a1>1:
        for xx in range(a1-1):
            if b!='':
                b+=','
            b+=str(a[x]+1+xx)
print("Output:-\nThe given arrya: \t",a,"\n and the missing numbers : ",b)

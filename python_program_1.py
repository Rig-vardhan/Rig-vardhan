print("Print all non repeating elements form an given array.\n")

# function for sorting --------------

def sort(b):
    z=0
    for xx in range(len(b)-1):
        z+=1
        for x in range(0,len(b)-z):
            if b[x]>b[x+1]:
                b[x],b[x+1]=b[x+1],b[x]

# function for sorting end--------------

print("Enter the numbers separated by comma.\nExample : 1,2,3,45\n Pres Enter after last number.")
b=list(eval(input("Numbers :")))
sort(b)
d=[]
a=list(b)
print("List of non repeating elements : ",end="")
c=0
for x in a:
    z=0
    #print("1=======\nx=",x,"\na=",a)
    for y in b[c:len(b)]:
        if x==y:
            z=z+1
    c+=z
    if z==1:
        d.append(x)
for x in range(len(d)):
    print(d[x],end="")
    if x!=len(d)-1:
        print(",",end="")

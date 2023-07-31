
# Q 2. Sort the element from two different array and out put should be single sorted array.

def sort(aa):
    z=0
    for xx in range(len(aa)-1):
        z+=1
        for x in range(0,len(aa)-z):
            if aa[x]>aa[x+1]:
                aa[x],aa[x+1]=aa[x+1],aa[x]
def remain(q,r):
    for x in range(q,len(r)):
        c.append(r[x])
        
#a=[9,4,9,6,7]      #b=[1,3,8]
c=[]
i=ii=0
a=list(eval(input("Enter the first arrya :")))
b=list(eval(input("Enter the second arrya :")))
sort(a) # sorting first arrya
sort(b) # sorting second arrya
while i<len(a) or ii<len(b):
    if i==len(a):
        remain(ii,b)
        break
    elif ii==len(b):
        remain(i,a)
        break
    elif a[i]>b[ii]:
        c.append(b[ii])
        ii+=1
    elif a[i]<b[ii]:
        c.append(a[i])
        i+=1
    elif a[i]==b[ii] :
        c.append(b[ii])
        c.append(a[i])
        i+=1
        ii+=1

print("Sorted Arya : \n")
c=str(c)
for x in range(1,len(c)-1):
    print(c[x],end="")






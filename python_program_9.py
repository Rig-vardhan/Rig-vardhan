#       Q. First longest increasing sequence in an array
a=list(eval(input("Enter the arrya :")))

#a=[5, 6, 7, 1, 2, 3, 4, 2, 3, 4, 5, 6, 7]
c=0
for x in range(len(a)-1):
    if a[x]==(a[x+1]-1):
        b1=x
        b=0
        for xx in range(x,len(a)-1):
            if a[xx]==(a[xx+1]-1):
                b+=1
            else:
                break
        if b>c:
            c=b
            c1=b1
print("The longest increasing sequence in an array :")            
for x in range(c+1):
    print(a[c1+x],end="")
    if x <c:
        print(",",end="")

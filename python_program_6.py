
#      Q. 1: Arrange the zeros to right and ones to left

a=list(eval(input("Enter the arrya :")))
b=0
for x in a:
    b+=x
print("Output :- ")
c=[]
for x in range(len(a)):
    if x < b:
        c.append(1)
    else :
        c.append(0)
c=str(c)
for x in range(1,len(c)-1):
    print(c[x],end="")

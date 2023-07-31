## To get the sum of odd and even elements.

print("IT will Print the sum of odd and even elements.\n")

print("Enter the numbers separated by comma.\nExample : 1,2,3,45\n Pres Enter after last number.")
b=list(eval(input("Numbers :")))
a,c=0,0
for x in b:
    if x%2==0:
        a+=x
    else :
        c+=x
print("\n Sum of odd elements  =",c)
print("\n Sum of even elements =",a)

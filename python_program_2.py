print(" Print consecutive elements in array which sum is equal to given sum.\n")

print("Enter the numbers separated by comma.\nExample : 1,2,3,45\n Pres Enter after last number.")
#b=(1, 2, 3, 4, 4,6,10, 5,  5, 2, 3, 5, 2, 5, 2)
b=eval(input("Numbers :"))
a=int(input("Sum of Elements :"))
for x in range(len(b)-1):
    a1=0
    if b[x] < a:
        for xx in range(x,len(b)):
            if a1==a:
                for b1 in range(x,xx-1):
                    print(b[b1],"+ ",end="")
                print(b[xx-1],end="")
                print(" =",a)
                a1=0
                break
            elif a1>a :
                a1=0
                break
            else :
                a1+=b[xx]
        
print("This element are conservative elements because\n they are stored inside the list and")
print("List access the elements by their index value.")

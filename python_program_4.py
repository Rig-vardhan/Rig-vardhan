# Q 1. Occurrence of the given element in the array.

print("Occurrence of the given element in the array.\n")
def counting(xx):
    c=0
    for x in xx:
        if x==b:
            c+=1
    return c

a=eval(input("Enter the arrya :"))
a=list(a)
b=int(input("Enter the element :"))

# c=a.count(b) //The count() method returns the number of times [element] appears in the list.

c=counting(a)
if c>0:
    d="The element {} occurred {} times in the arrya."
    print(d.format(b,c))
else :
    d="The number {} is not the element of arrya"
    print(d.format(b))

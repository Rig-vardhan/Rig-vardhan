# functions for pramide Formation.
print("\t\t This program is based on Pramide Formation Types .")


def star_Pyramid_1(a):
    b=0
    for x in range(a):
        b=b+1
        for y in range(a-b):
            print(" ",end="")
        for z in range(b):
            print("* ",end="")
        print(" ")
        
#star_Pyramid_1(int(input("Enter total number of rows in pramide : ")))   
"""
output of star_Pyramid_1:-

   *  
  * *  
 * * *  
* * * *
"""


def star_Pyramid_2(a):
    b=0
    for x in range(a):
        b=b+1
        print(" "*(a-b),end="")
        print("* "*b)

#star_Pyramid_2(int(input("Enter total number of rows in pramide : ")))

"""
output star_Pyramid_2:-

   * 
  * * 
 * * * 
* * * *

"""

def star_Pyramid_3(a):
    b,c=0,1
    for x in range(a):
        b=b+1
        print(" "*(a-b),end="")
        print("*"*(c))
        c=c+2

#star_Pyramid_3(int(input("Enter total number of rows in pramide : ")))
"""

output star_Pyramid_3:-

   *
  ***
 *****
*******

"""
#===============================================================================
def alphabet_Pyramid_1(a):
    b,c,ascii_value=0,1,65
    for x in range(a):
        b=b+1
        print(" "*(a-b),end="")
        print(chr(ascii_value)*(c))
        c=c+2
        ascii_value=ascii_value+1

#alphabet_Pyramid_1(int(input("Enter total number of rows in pramide : ")))

"""

output alphabet_Pyramid_1:-

   A
  BBB
 CCCCC
DDDDDDD

"""

def alphabet_Pyramid_2(a):
    b=0
    ascii_value=65
    for x in range(1,a+1):
        b=b+1
        print("  "*(a-b),end="")
        for y in range(x):
            print(chr(y+ascii_value),end=" ")
        for y in range(x-1,0,-1):
            print(chr(y+ascii_value-1),end=" ")
        print("")

#alphabet_Pyramid_2(int(input("Enter total number of rows in pramide : ")))

"""

output alphabet_Pyramid_2:-

        A 
      A B A 
    A B C B A 
  A B C D C B A 
A B C D E D C B A
"""

def alphabet_Pyramid_3(a):
    b=0
    ascii_value=64
    for x in range(a):
        b=b+1
        print("  "*(a-b),end="")
        c=b
        for y in range((c+(c-1))):
            if y<c:
                x=x+1
                print(chr(x+ascii_value),end=" ")
            else:
                x=x-1
                print(chr(x+ascii_value),end=" ")
        print("")

#alphabet_Pyramid_3(int(input("Enter total number of rows in pramide : ")))

"""

output alphabet_Pyramid_3:-
        A 
      B C B 
    C D E D C 
  D E F G F E D 
E F G H I H G F E
"""

#==============================================================================

def numeric_Pyramid_1(a):
    b=0
    for x in range(a):
        b=b+1
        print(" "*(a-b),end="")
        c=b
        for y in range((c+(c-1))):
            if y<c:
                x=x+1
                print(x,end="")
            else:
                x=x-1
                print(x,end="")
        print("")

#numeric_Pyramid_1(int(input("Enter total number of rows in pramide : ")))
"""

output numeric_Pyramid_1:-    
    1
   232
  34543
 4567654
567898765
"""

def numeric_Pyramid_2(a):
    a,b=5,0
    for x in range(a):
        b=b+1
        print("  "*(a-b),end="")
        c=b
        for y in range((c+(c-1))):
            if y<c:
                x=x+1
                print(x,end=" ")
            else:
                x=x-1
                print(x,end=" ")
        print("")

#numeric_Pyramid_2(int(input("Enter total number of rows in pramide : ")))

"""

output numeric_Pyramid_2:-   
        1 
      2 3 2 
    3 4 5 4 3 
  4 5 6 7 6 5 4 
5 6 7 8 9 8 7 6 5 
"""

def numeric_Pyramid_3(a):
    a,b=5,0
    for x in range(1,a+1):
        b=b+1
        print("  "*(a-b),end="")
        for y in range(x):
            print(y+1,end=" ")
        for y in range(x-1,0,-1):
            print(y,end=" ")
        print("")
        
#numeric_Pyramid_3(int(input("Enter total number of rows in pramide : ")))

"""
output numeric_Pyramid_3:-    
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 
"""



def all():
    a=int(input("Enter total number of rows in pramide : "))
    star_Pyramid_1(a)
    print('\n\n',"="*45,"\n\n")
    star_Pyramid_2(a)
    print('\n\n',"="*45,"\n\n")
    star_Pyramid_3(a)
    print('\n\n',"="*45,"\n\n")
    alphabet_Pyramid_1(a)
    print('\n\n',"="*45,"\n\n")
    alphabet_Pyramid_2(a)
    print('\n\n',"="*45,"\n\n")
    alphabet_Pyramid_3(a)
    print('\n\n',"="*45,"\n\n")
    numeric_Pyramid_1(a)
    print('\n\n',"="*45,"\n\n")
    numeric_Pyramid_2(a)
    print('\n\n',"="*45,"\n\n")
    numeric_Pyramid_3(a)
    print('\n\n',"="*45,"\n\n")
all()



#   American Standard Code for Information Interchange

#print all ascii value form 0 to 255 
digit = 0
while digit<=255:
    print("%d = %c\t\t" %(digit, chr(digit)),end='')
    print("%d = %c\t\t" %(digit+1, chr(digit+1)),end='')
    print("%d = %c\t\t" %(digit+2, chr(digit+2)),end='')
    print("%d = %c\t\t" %(digit+3, chr(digit+3)))
    digit += 4

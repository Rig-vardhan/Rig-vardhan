import random
#======================================================================================================
# game_type()

def warning():
    print("\n\n????????????????????????????????")  
    print("??Pleas enter the valid value ??")
    print("????????????????????????????????\n\n")
    
def note():
    print('\n\n**********************************')
    print('** This block is already filled **')
    print('**********************************\n\n')
#======================================================================================================
#======================================================================================================
def value_fix(a):
    a=a.upper()
    a=a.strip()
    return(a)
#======================================================================================================
#======================================================================================================
#

def exit_point():
    global y
    check=''
    user_input=y
    while type(check)!=int:
        if user_input.startswith("Q"):
            check=input("\nDO YOU WISH TO STOP PLAYING NOW (YES/NO): ")
            check=value_fix(check)
        else:
            check=input("\nWOULD YOU LIKE TO PLAY AGAIN (YES/NO): ")
            check=value_fix(check)
        if check.startswith("Y") and -1!="YES".find(check):
            check=1          
        elif check.startswith("N") and -1!="NO".find(check):  
            check=2
        else:
            warning()
    return(check)

#======================================================================================================

a=["         1          ","         2          ","         3          ",
   "         4          ","         5          ","         6          ",
   "         7          ","         8          ","         9          "]

#======================================================================================================

xx=["## ##          ## ##",
    "## ## ##    ## ## ##",
    "   ## ## ## ## ##   ",
    "      ## ## ##      ",
    "      ## ## ##      ",
    "   ## ## ## ## ##   ",
    "## ## ##    ## ## ##",
    "## ##          ## ##"]

#======================================================================================================

yy=["## ## ## ## ## ## ##",
    "## ## ## ## ## ## ##",
    "## ##          ## ##",
    "## ##          ## ##",
    "## ##          ## ##",
    "## ##          ## ##",
    "## ## ## ## ## ## ##",
    "## ## ## ## ## ## ##"]

#======================================================================================================
bb="                    ";
#======================================================================================================

r,p1,p2,rt,gt=0,0,0,0,0;

#======================================================================================================
def output():
    for c in range(3):
        for i in range(len(xx)):
            if aa[0+c*3]=="x" :
                print(xx[i],chr(12)*2,end=" ")
            elif aa[0+c*3]=="o" :
                print(yy[i],chr(12)*2,end=" ")
            else:
                if i!=3:
                    print(bb,chr(12)*2,end=" ")
                else:
                    print(a[0+c*3],chr(12)*2,end=" ")
            if aa[1+c*3]=="x" :
                print(xx[i],chr(12)*2,end=" ")
            elif aa[1+c*3]=="o":
                print(yy[i],chr(12)*2,end=" ")
            else:
                if i!=3:
                    print(bb,chr(12)*2,end=" ")
                else:
                    print(a[1+c*3],chr(12)*2,end=" ")

            if i<5 and c==0 and rt=="M":
                if aa[2+c*3]=="x" :
                    print(xx[i],end="   ")
                elif aa[2+c*3]=="o":
                    print(yy[i],end="   ")
                else:
                    if i!=3:
                        print(bb,end="   ")
                    else:
                        print(a[2+c*3],end="   ")
                if i==0 or i==2 or i==4:
                    print("\t","="*44)
                elif i==1:
                    print("\t ||Player||   X   ||   O   || Draw ||Round ||")
                elif i==3:
                    print("\t ||Points||   {0:^2}  ||   {1:^2}  ||  {2:^2}  ||  {3:^2}  ||".format(p1,p2,r-(p1+p2),r+1))
            else:    
                if aa[2+c*3]=="x" :
                    print(xx[i])
                elif aa[2+c*3]=="o":
                    print(yy[i])
                else:
                    if i!=3:
                        print(bb)
                    else:
                        print(a[2+c*3])
        if c!=2:
            for z in range(2):
                for i in range(68):
                   print(chr(12),end="")
                print("\t\t\t")
                
#======================================================================================================
                
def value():
        if aa[y-1]!="X" or aa[y-1]!="o":
            if (1+r)%2!=0:
                if (1+i)%2!=0: aa[y-1]="x";
                else: aa[y-1]="o";
            else:
                if (1+i)%2!=0: aa[y-1]="o";
                else: aa[y-1]="x";
                
#======================================================================================================

def winer():
    global win    
    if aa[0]==aa[4]==aa[8]:
        win=1;
    elif aa[6]==aa[4]==aa[2]:
        win=1;
    else:
        for c in range(3):
            if aa[0+c*3]==aa[1+c*3]==aa[2+c*3]:
                win=1;
                break
            elif  aa[0+c]==aa[3+c]==aa[6+c]:
                win=1;
                break

#======================================================================================================
            
def  intro():       
   message_1="""    WELCOME TO

               Tic    Tac   Toe
                   |      |
              __X__|___O__|__X__
                   |      |
              __O__|___X__|__O__
                   |      |
                X  |   O  |  X
            """
   print(message_1)
#======================================================================================================
def game_type():
   global gt
   message_2="""
            Game type:->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            >>                                                >>
            >> (S) Single player (Player X VS Coumputer O)    >>
            >>                                                >>
            >> (M) Multiplayer  (Player X VS Player O )       >>
            >>                                                >>
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            """
   print(message_2)
   while 1:
    gt=input("Game type ( S / M ):")
    gt=value_fix(gt)
    if 'S'==gt or 'M'==gt:
        break
    else:
        warning()
#================================================================================================
def round_type():
   global rt
   message_3="""
            Round type:->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            >>                                              >>
            >> (S) Single round    OR   (M) Multiple round  >>
            >>                                              >>
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

                 * NOTE -: By default Round type is [(M) Multiple round ]
                           Press ( ENTER ) to continue with default option. 
            """
   print(message_3) 
   while 1:
     rt=input("Round type ( S / M ):")
     rt=value_fix(rt)
     if 'S'==rt or 'M'==rt :
         break
     elif rt=='':
         rt='M'
         break
     else:
         warning()      
#======================================================================================================
def game_move():
    global y,aa
    
    # prog for cross
    if aa[4]!='y':
        a=[0,4,8]
        b=[2,4,8]
        d=0
        for c in range(3):
            if aa[a[c]]=='x':
                d+=1
        if d==2:
            for c in range(3):
                if type(aa[a[c]])==int:
                    y=a[c]
                    return(1)
        d=0
        for c in range(3):
            if aa[b[c]]=='x':
                d+=1
        if d==2:
            for c in range(3):
                if type(aa[b[c]])==int:
                    y=b[c]
                    return(1)

    # prog for vertical    
    for f in range(3):
            b=f
            c=0
            if aa[b]=='x':
                c+=1
            elif aa[b]=='y':
                continue
            for d in range(2):
                b+=3
                if aa[b]=="x":
                    c+=1
                elif aa[b]=='y':
                    continue
            if c==2:
                b=f
                if type(aa[b])==int:
                    y=b
                    return(1)
                for e in range(2):
                    b+=3
                    if type(aa[b])==int:
                        y=b
                        return(1)


    # prog for horizontal
    for b in range(3):
        d=0
        for c in range(3):
            c+=b*3
            if aa[c]=='x':
                d+=1
            elif aa[c]=="y":
                continue
        if d==2:
            for f in range(3):
                f+=b*3
                if type(aa[f])==int:
                    y=f
                    return(1)
    return(0)
###################################################################################
def computer_input():
    global y,aa
    a=game_move()
    if a!=1:
        co="computer input";
        while(1):
            co=random.choice(aa)
            if(type(co)==int):
                y=co;
                break
    else:
        y+=1






#======================================================================================================
def menu():
    global r,p1,p2,rt,gt,aa,y,win,lable_1
    message_4="""
            ======================
            [         MENU       ]
            ======================                
            [ Resume game  :  RG ]
            [ New Game     :  NG ]
            
            [ Game type    :  GT ] 
            [ Round type   :  RT ]
            [ Quit         :  Q  ]
            ======================
            """
    while(1):
        print(message_4)
        var=input('Enter your\'r option :')
        var=value_fix(var)
        if var=="RG":
            print('\n\n\n\n\n\n')
            output()
            if gt=='M':
                print(lable_1)
            else:
                print("Player X ")
            return(var)
        elif var=="NG":
            print('\n\n\n\n\n\n')
            r,p1,p2,rt,gt=0,0,0,0,0
            y,win=0,0
            aa=[1,2,3,4,5,6,7,8,9]
            return(var)
        elif var=='GT':
            print('\n\n\n\n\n\n')
            r,p1,p2=0,0,0
            y,win=0,0
            aa=[1,2,3,4,5,6,7,8,9]
            check=gt
            print("\nif you change the game type. The Game will restart\n Press Enter")
            input()
            game_type()
            if check!=gt:
                return('NG')
        elif var=='RT':
            print('\n\n\n\n\n\n')
            r,p1,p2=0,0,0
            y,win=0,0
            aa=[1,2,3,4,5,6,7,8,9]
            check=rt
            print("\n  If you change the round type. The Game will restart\n Press Enter")
            input()
            round_type()
            if check!=rt:
                return('NG')
        elif var.startswith("Q") and -1!="QUIT".find(var):
            y='QUIT'
            print('\n\n\n\n\n\n')
            return(exit_point())
        else:
            warning()
#======================================================================================================
def player_input():    
    while 1:
        global y
        print(aa,'\n NOTE ::  Enter ( M ) for MENUE \n')
        b=input('Enter your\'r choice :')
        b=value_fix(b)
        if b.startswith("M") and -1!="MENUE".find(b):
            b=menu()
            if b=="RG":
                continue
            elif b=='NG':
                return(b)
            elif b==1:
                #Quit
                return(y)
            else:
                continue
        b=b[0]
        b=ord(b)
        if b>48 and b<58 :
            b-=48
            if b in aa:
                return (b)
            else:
                note()
                input('\n[Press Enter]\n\n\n\n\n\n')
                output()
        else:
            warning()
            input('\n[Press Enter]\n\n\n\n\n\n')
            output()
#======================================================================================================
#======================================================================================================
       
while(1):
    global aa,y,win,lable_1
    y,win=0,0
    aa=[1,2,3,4,5,6,7,8,9]
    if gt==0 and rt==0:
        intro()
    if gt==0:
        game_type()
    if rt==0:
        round_type()
    output()
    for i in range(9):
        if gt=="M":
            if (1+r)%2!=0:        
                if (1+i)%2!=0: lable_1="Player X"
                else: lable_1="Player O"
            else:
                if (1+i)%2!=0: lable_1="Player O"
                else: lable_1="Player X"
            print(lable_1)
            y=player_input()
        elif gt=="S":
            if (1+r)%2!=0:        
                if (1+i)%2!=0:
                    print("Player X")
                    y=player_input()
                else:
                    computer_input()    
            else:
                if (1+i)%2!=0:
                    computer_input()    
                else:
                    print("Player X")
                    y=player_input()
        if y=='QUIT' or y=='NG':                   # To break for loop..
            break
        else:
            y=int(y)
        value()
        output()
        print('\n')
        winer()
        if win!=0 and rt=="M":
            if (1+r)%2!=0:        
                if (1+i)%2!=0: p1=p1+1;
                else: p2=p2+1;
                break
            else:
                if (1+i)%2!=0: p2=p2+1;
                else: p1=p1+1;
                break
        elif win!=0 and rt=="S":
            if (1+r)%2!=0:        
                if (1+i)%2!=0: print("\tPLAYER X IS WINER\n\n");
                else: print("\tPLAYER O IS WINER\n\n");
                break
            else:
                if (1+i)%2!=0: print("\tPLAYER O IS WINER\n\n");
                else: print("\tPLAYER X IS WINER\n\n");
                break
            break
        elif win==0 and i==8 :
            print("\tTHE GAME IS DRAW\n\n")
    if y=='QUIT':                               # To break while loop..
        break
    elif y=='NG':
        continue
    if rt=="S":
        y='check'
        y=exit_point()
        if y==2:
            break
        print('\n'*20)
    else:
        r=r+1;
print("THANK YOU\n I hope you enjoyed..")

#======================================

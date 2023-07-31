#==============================================================
#==============================================================
# This program is based on ROCK PAPER SCISSORE GAME
#==============================================================
#==============================================================
print('\t ** This program is based on ROCK PAPER SCISSORE GAME **')
def warning():
    print("\n\n????????????????????????????????")  
    print("??Pleas enter the valid value ??")
    print("????????????????????????????????\n\n")

def option():
    print("\n\t======== OPTION =========")
    print("\t||",list_1[0],"     : ",list_2[0]," ||\n\t||",list_1[1],"    : ",list_2[1]," ||\n\t||",list_1[2],"    : ",list_2[2]," ||")
    print("\t========================")
    print("\n*To check the Score Board Enter : SB\n")

def value_fix(a):
    a=a.upper()
    a=a.strip()
    return(a)

def option_and_score_board():   
    print("\n\t======== OPTION =========",'\t'*5,"|============== SCORE BOARD ========================|")
    print("\t||",list_1[0],"     : ",list_2[0]," ||",'\t'*5,"| Player    ||  WIN  ||  LOSE  || DRAW   || ROUNDS  |")
    print("\t||",list_1[1],"    : ",list_2[1]," ||",'\t'*5,"|---------------------------------------------------|")
    print("\t||",list_1[2],"    : ",list_2[2]," ||",'\t'*5,"| YOU       ||  {:3d}".format(list_3[0])," ||   {:3d}".format(list_3[1])," ||        ||         |")
    print("\t=========================",'\t'*5,"|--------------------------------  {:3d}".format(list_3[2]),"  --  {:3d}".format(sum(list_3)),"   |")
    print('\t'*9,"| COUMPUTER ||  {:3d}".format(list_3[1])," ||   {:3d}".format(list_3[0])," ||        ||"," "*7,"|")
    print('\t'*9,"|===================================================|")

def score_board():
    print("|============== SCORE BOARD ========================|")
    print("| Player    ||  WIN  ||  LOSE  || DRAW   || ROUNDS  |")
    print("|---------------------------------------------------|")
    print("| YOU       ||  {:3d}".format(list_3[0])," ||   {:3d}".format(list_3[1])," ||        ||         |")
    print("|--------------------------------  {:3d}".format(list_3[2]),"  --  {:3d}".format(sum(list_3)),"   |")
    print("| COUMPUTER ||  {:3d}".format(list_3[1])," ||   {:3d}".format(list_3[0])," ||        ||"," "*7,"|")
    print("|===================================================|")
    input("\n To close Score Board Press [(Enter)]")

def exit_point():
    check=" "
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


def game_type():
    print('which type of game you would like to play :-')
    print('==============================================================')
    print('|| Single round     || S : Single                           ||')
    print('||                                                          ||')
    print('|| Multiple round   || M : Multiple                         ||')
    print('==============================================================')
    print("\n * BY default it will select Multiple Round  \n - To select the default option press [(Enter)]")
    while 1:
        GT=input('Enter your game type : ')
        GT=value_fix(GT)
        if GT.startswith("S") and -1!='SINGLE'.find(GT):
            gt='S'
            break
        elif GT.startswith("M") and -1!='MULTIPLE'.find(GT) or GT=='':
            GT='M'
            break
        else:
            warning()
    gt=GT
    return (GT)



import random
list_1=['ROCK    ','PAPER    ','SCISSORE ','QUITE']
list_2=['R','P','S','Q']
# score_board values
list_3=[0,0,0]   
input_type='valid'
v2=1
win='\t\t'+(' '*13)+'YOU  WIN'
lose='\t\t'+(' '*13)+"YOU  LOSE"
print("******************************   Wellcome to the game    ***********************")
gt=game_type()#======================
while 1:
 if gt=='S':
     option()
 elif gt=='M':
     option_and_score_board()
 print('\n* To change the game type Enter :GT\n')
 print("\n*To quit the Game Enter :",list_2[3],'\n')
 if input_type!='valid':
     warning()
 v1=random.randint(0,2)
 user_input=input('Enter your choice : ')
 user_input=value_fix(user_input)
 if user_input.startswith("R") and -1!=list_1[0].find(user_input):
  v2=1
  input_type='valid'
 elif user_input.startswith("P") and -1!=list_1[1].find(user_input):
  v2=2
  input_type='valid'
 elif user_input.startswith("S") and -1!=list_1[2].find(user_input):
  v2=3
  input_type!='valid'
 elif user_input.startswith("SCO") and -1!='SCORE BOARD'.find(user_input) or user_input=="SB":
  score_board()
  input_type='valid'
  continue
 elif user_input.startswith("G") and -1!='GAME TYPE'.find(user_input) or user_input=="GT":
  gt=game_type()
  input_type='valid'
  continue
 elif user_input.startswith("Q") and -1!=list_1[3].find(user_input):
     check=exit_point()
     if check==1:
        break
     elif check==2:
        input_type='valid'
        continue
 else:
  input_type='not valide'
  continue

 v2-=1
 print("\n\n\t\t player\t\tvs\t    computer\n\n","\t\t",list_1[v2],'\t \t   ',list_1[v1],"\n")
 print("\t\t#####################################")
 if v1==v2:
   print("\t\t##     The game has been draw      ##")
   list_3[2]+=1
 elif v1==2 :
     if v1==2 and v2==0 :
       print(win)
       list_3[0]+=1
     else:
       print(lose)
       list_3[1]+=1
 elif v1==1 :
     if v1==1 and v2==2 :
       print(win)
       list_3[0]+=1
     else:
       print(lose)
       list_3[1]+=1
 elif v1==0 :
     if v1==0 and v2==1 :
       print(win)
       list_3[0]+=1
     else:
       print(lose)
       list_3[1]+=1
 print("\t\t#####################################\n\n\n")
 if gt=='S':
     check=exit_point()
     if check==2:
         user_input=list_1[3]
         final=exit_point()   # final option.
         if final==1:
             break
     print("\n\n******************************  NEXT ROUND    ***********************")
 else:
     print("\n\n******************************  NEXT ROUND    ***********************")
print("\n\n******************************  GAME CLOSED    ***********************")



#============================================================================================================
#============================================================================================================
#============================================================================================================
#============================================================================================================



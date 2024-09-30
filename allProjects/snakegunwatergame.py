import random as rn
comp=['s','w','g']
print("*******************Snake Water Gun Game****************************")
s='s'
w='w'
g='g'
print("press 1 for start")
a=int(input())
point=0
comp_point=0
count=0
while True:
    if(a==1):
        print("press s for snake")
        print("press w for water")
        print("press g for gun")
        count=count+1
        st=input("you      =  ")
        if(st=='s'):
            k=rn.choice(comp)
            print("computer = ",k)
            if(st==k):
                print("DRAW\n")
            elif(k=='w'):
                print("WIN\n")
                point=point+1
            else:
                print("LOSE\n")
                comp_point=comp_point+1     
        if(st=='w'):
            k=rn.choice(comp)
            print("computer = ",k)
            if(st==k):
                print("DRAW\n")
            elif(k==s):
                print("LOSE\n")
                comp_point=comp_point+1
               
            else:
                print("LOSE\n")
                point=point+1    
        if(st=='g'):
            k=rn.choice(comp)
            print("computer = ",k)
            if(st==k):
                print("DRAW\n")
            elif(k=='s'):
                print("WIN\n")
                point=point+1
            
            else:
                print("LOSE\n")
                comp_point=comp_point+1
              
        if(point==5):
            print("***************you win******************")
            print("______________Score__________________")
            print("your point : ",point)
            print("computer point : ",comp_point)
            print(f"You won in {count} attempt")
            break
        elif(comp_point==5):
            print("**************computer win****************")
            print("______________Score__________________")
            print("your point     : ",point)
            print("computer point : ",comp_point)
            print(f"Computer Won in {count} attempt")
            break
        else:
           continue
    else:
        print("invalid input..")
        break
    
            
                
            
            

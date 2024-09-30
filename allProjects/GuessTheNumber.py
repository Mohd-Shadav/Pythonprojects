import random

def Guess():
   count = 0 

   while(True):
        i = int(input("Guess The Number between 1 - 10 : "))         
        r = random.randint(1,10) 
    #   print(r)
        if(r==i):
          print(f'Your answer is correct ✅\nyour guess : {i}\nActuall   Number : {r}')
          print(f'You Win at {count+1} attempt 😎')
          i = input("press 1 to play More or Any key to exit : ")
          if(i=="1"):
              count = 0
              continue
          else: 
              exit()
        else:
          print(f'Your answer is wrong ❌\nyour guess : {i}\nActuall  Number : {r}')
          count += 1
        if(count==5):
          print("You Lost 😫")
    #    print("press 1 to play Again or Any key to exit")
          i = input("press 1 to play Again or Any Key to exit : ")
          if(i=="1"):
              count = 0
              continue
          else: 
              exit()
           

if __name__ == "__main__":

    Guess()

  
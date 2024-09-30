print("1.Men")
print("2.Women")
print("3.Kids")
Num=int(input("Enter Choice : "))
print("---------------------------------------------------------------")
bag=[]
collection=["Mens",'Women','Kids']
if(Num==1):
    print("1.Formal")
    print("2.Casual")
    print("3.PartyWear")
    Formal={'Shirts':1000,'Trouser':1500,'formal shoes':1000,'Tie':300}
    Casual={"T-shirts":500,'Jeans':700,"lower":500,'sportswatch':550}
    PartyWear={"Blazer":2500,"Sherwani":3000,"3-pieces Suit":10000,"juti":2000,}
    option=int(input("Enter Category : "))
    print("---------------------------------------------------------------")
    if(option==1):
        while True:
            
            for x in Formal:
                print(x,"= Rs.",Formal[x],"/each")
            print("---------------------------------------------------------------")
            print("1.shirt")
            print("2.trouser")
            print("3.formal shoes")
            print("4.tie")
            print("5.Bill")
            pick=int(input("pick up,what do you want : "))
            print("---------------------------------------------------------------")
            if(pick==1):
                bag.append(1000)
                print("#Shirt Add into the bag!Anything Else")
                continue
            if(pick==2):
                bag.append(1500)
                print("#Trouser Add into the bag!Anything Else")
                continue
            if(pick==3):
                bag.append(1000)
                print("#Shoes Add into the bag!Anything Else")
                continue
            if(pick==4):
                bag.append(300)
                print("#Tie Add into the bag!Anything Else")
                continue
            if(pick>=5):
                print(bag)
                print("your Bill : RS.",sum(bag)) 
                break
    
    if(option==2):
        while True:
            for x in Casual:
                print(x,"= Rs.",Casual[x],"/each")
            print("---------------------------------------------------------------")
            print("1.T-shirt")
            print("2.Jeans")
            print("3.Lower")
            print("4.SportsWatch")
            print("5.Bill")
            pick=int(input("pick up,what do you want : "))
            print("---------------------------------------------------------------")
            if(pick==1):
                bag.append(500)
                print("#T-Shirt Add into the bag!Anything Else")
                continue
            if(pick==2):
                bag.append(700)
                print("#Jeans Add into the bag!Anything Else")
                continue
            if(pick==3):
                bag.append(500)
                print("#Lower Add into the bag!Anything Else")
                continue
            if(pick==4):
                bag.append(550)
                print("#SportsWatch Add into the bag!Anything Else")
                continue
            if(pick>=5):
                print(bag)
                print("your Bill : RS.",sum(bag)) 
                break
    if(option==3):
        while True:
            for x in PartyWear:
                
                print(x,"= Rs.",PartyWear[x],"/each")
            print("---------------------------------------------------------------")
            print("1.Blazer")
            print("2.Sherwani")
            print("3.3-pieces Suit")
            print("4.Juti")
            print("5.Bill")
            pick=int(input("pick up,what do you want : "))
            print("---------------------------------------------------------------")
            if(pick==1):
                
                bag.append(2500)
                print("#Blazer Add into the bag!Anything Else")
                continue
            if(pick==2):
                bag.append(3000)
                print("#Sherwani Add into the bag!Anything Else")
                continue
            if(pick==3):
                bag.append(10000)
                print("#3-pieces suit Add into the bag!Anything Else")
                continue
            if(pick==4):
                bag.append(2000)
                print("#Juti Add into the bag!Anything Else")
                continue
            if(pick>=5):
                print(bag)
                print("your Bill : RS.",sum(bag)) 
                break
if(Num==2):
    print("1.Suits")
    print("2.Sarees")
    print("3.PartyWear")
    Suits={'Punjabi Salwar Suit':1499,'Simple':999,'Pashmina Salwar Suit':1999,'Gagra Choli':2999}
    Sarees={"Simple Saree":699,'Silk Saree':1999,"Banarsi Saree":2499,'Blouse':499}
    PartyWear={"Gown":4999,"Lehnga":3999,"juti":2000,}
    option=int(input("Enter Category : "))
    print("---------------------------------------------------------------")
    if(option==1):
        while True:
            
            for x in Suits:
                print(x,"= Rs.",Suits[x],"/each")
            print("---------------------------------------------------------------")
            print("1.Punjabi Salwar Suit")
            print("2.Simple")
            print("3.Pashmina Salwar Suit")
            print("4.Gagra Choli")
            print("5.Bill")
            pick=int(input("pick up,what do you want : "))
            print("---------------------------------------------------------------")
            if(pick==1):
                bag.append(1499)
                print("#Punjabi Salwar Suit Add into the bag!Anything Else")
                continue
            if(pick==2):
                bag.append(999)
                print("#Simple Add into the bag!Anything Else")
                continue
            if(pick==3):
                bag.append(1999)
                print("#Pashmina Salwar Suit Add into the bag!Anything Else")
                continue
            if(pick==4):
                bag.append(2999)
                print("#Gagra Choli Add into the bag!Anything Else")
                continue
            if(pick>=5):
                print(bag)
                print("your Bill : RS.",sum(bag)) 
                break
    
    if(option==2):
        while True:
            for x in Sarees:
                print(x,"= Rs.",Sarees[x],"/each")
            print("---------------------------------------------------------------")
            print("1.Simple Saree")
            print("2.Silk Saree")
            print("3.Banarsi Saree")
            print("4.Blouse")
            print("5.Bill")
            pick=int(input("pick up,what do you want : "))
            print("---------------------------------------------------------------")
            if(pick==1):
                bag.append(699)
                print("#Simple Saree Add into the bag!Anything Else")
                continue
            if(pick==2):
                bag.append(1999)
                print("#Silk Saree Add into the bag!Anything Else")
                continue
            if(pick==3):
                bag.append(2499)
                print("#Banarsi Saree Add into the bag!Anything Else")
                continue
            if(pick==4):
                bag.append(499)
                print("#Blouse Add into the bag!Anything Else")
                continue
            if(pick>=5):
                print(bag)
                print("your Bill : RS.",sum(bag)) 
                break
    if(option==3):
        while True:
            for x in PartyWear: 
                print(x,"= Rs.",PartyWear[x],"/each")
            print("---------------------------------------------------------------")
            print("1.Gown")
            print("2.Lehnga")
            print("3.Juti")
            print("4.Bill")
            pick=int(input("pick up,what do you want : "))
            print("---------------------------------------------------------------")
            if(pick==1):
                
                bag.append(4999)
                print("#Gown Add into the bag!Anything Else")
                continue
            if(pick==2):
                bag.append(3999)
                print("#Lehnga Add into the bag!Anything Else")
                continue
            if(pick==3):
                bag.append(2000)
                print("#Juti Add into the bag!Anything Else")
                continue
            if(pick>=4):
                print(bag)
                print("your Bill : RS.",sum(bag)) 
                break
if(Num==3):
    print("1.Boy")
    print("2.Girl")
    Boy={'Baba Suit':1499,'T-Shirt':499,'Shirt-Jeans':1499,'Shoes':999}
    Girl={"Jeans-Top":999,'Skirt':999,"Frock":1299,'Sandals':799}
    option=int(input("Enter Category : "))
    print("---------------------------------------------------------------")
    if(option==1):
        while True: 
            for x in Boy:
                print(x,"= Rs.",Boy[x],"/each")
            print("---------------------------------------------------------------")
            print("1.Baba Suit")
            print("2.T-Shirt")
            print("3.Shirt-Jeans")
            print("4.Shoes")
            print("5.Bill")
            pick=int(input("pick up,what do you want : "))
            print("---------------------------------------------------------------")
            if(pick==1):
                bag.append(1499)
                print("#Baba Suit Add into the bag!Anything Else")
                continue
            if(pick==2):
                bag.append(499)
                print("#T-shirt Add into the bag!Anything Else")
                continue
            if(pick==3):
                bag.append(1499)
                print("#Shirt-Jeans Add into the bag!Anything Else")
                continue
            if(pick==4):
                bag.append(999)
                print("#shoes Add into the bag!Anything Else")
                continue
            if(pick>=5):
                print(bag)
                print("your Bill : RS.",sum(bag)) 
                break
    
    if(option==2):
        while True:
            for x in Girl:
                print(x,"= Rs.",Girl[x],"/each")
            print("---------------------------------------------------------------")
            print("1.Jeans-Top")
            print("2.Skirt")
            print("3.Frock")
            print("4.Sandals")
            print("5.Bill")
            pick=int(input("pick up,what do you want : "))
            print("---------------------------------------------------------------")
            if(pick==1):
                bag.append(999)
                print("#Jeans-Top Add into the bag!Anything Else")
                continue
            if(pick==2):
                bag.append(999)
                print("#Skirt Add into the bag!Anything Else")
                continue
            if(pick==3):
                bag.append(1299)
                print("#Frock Saree Add into the bag!Anything Else")
                continue
            if(pick==4):
                bag.append(799)
                print("#Sandals Add into the bag!Anything Else")
                continue
            if(pick>=5):
                print(bag)
                print("your Bill : RS.",sum(bag)) 
                break
  
        
        
                
        
          
          
       

        
        
    

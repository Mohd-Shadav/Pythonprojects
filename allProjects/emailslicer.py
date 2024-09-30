import re
def Email():
    email = input("Enter Email : ")
    c=re.findall(("\S[a-z]\S\d\S[@.]\S"),email)
    

    if(len(c)!=0):
        l=email.split("@")
        print(f"your Username is : {l[0]+'CS'}")
    
    else:
        print("no")

Email()
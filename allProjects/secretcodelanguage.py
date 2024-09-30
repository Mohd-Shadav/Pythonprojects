import random
a="this is a secret code language you may need to decode this to read"
x=a.split()
b='atr ctt vvf but gfg ffd dss sss agt ayy wpl eyw rsa tvv ydh yvb t6y '
b=b.split()
code=[]
#print(x[0])
for i in range(len(x)):
    #print(x[i],end=' ')
    
    if(len(x[i])<=3):
        n=x[i][::-1]
        code.append(n)
      
    else:
        #x[i][0]                                                      
        m=x[i].removeprefix(x[i][0])
        m=m+x[i][0]
        m=random.choice(b)+m+random.choice(b)
        #print(m,end=' ')
        code.append(m)
s=' '.join(code)
print(s)


        
        

list1=["1.What is the output of the expression : 3*1**3\n",
       "2.Which of the following function convert a string to a float in python?\n",
       "3.What data type is the object below ? L = [1, 23, ‘hello’, 1]\n",
       "4.Which of these is not a core data type?\n",
       "5.Suppose list1 is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after list1.pop(1)\n",
       "6.What is called when a function is defined inside a class?\n",
       "7.What is the output of the following segment: chr(ord('A'))\n",                 
       "8.What is the output of the following code :L = ['a','b','c','d'] print("".join(L))\n",
       "9.What will be the output of the following code :print type(type(int))\n",
       "10.Which one of these are the difference of print() and return"]
list2={list1[0]:3,list1[1]:"float(x)",list1[2]:"List",list1[3]:"class\n"
       ,list1[4]:"[3,5, 20, 5, 25, 1, 3]",list1[5]:"Method",list1[6]:"A\n"
       ,list1[7]:"abcd",list1[8]:"type\'type\'",list1[9]:"print stores the value but return not"}
print("-----------------------Question for Rs.10,000---------------------")
print(list1[0])
print("a. 27","\nb. 1",'\nc.',list2[list1[0]],"\nd. 0")
answer=input("Your Answer : ")
if(answer=='c'):
    print("Right Answer!!!You won Rs.10,000")
    print("-----------------------Next Question for Rs.20,000---------------------------")
    print(list1[1])
    print("a. int(x [,base])","\nb.",list2[list1[1]],'\nc. str(x)',"\nd. long(x [,base] )")
    answer=input("Your Answer : ")
    if(answer=='b'):
        print("Right Answwer!!!You won Rs.20,000")
        print("-----------------------checkpoint Question for Rs.50,000---------------------------")
        print(list1[2])
        print("a.",list2[list1[2]],"\nb. tuple",'\nc. dict',"\nd. set")
        answer=input("Your Answer : ")
        if(answer=='a'): 
            print("Right Answer!!!You won Rs.50,000")
            print("-----------------------Next Question for Rs.100,000---------------------------")
            print(list1[3])
            print(f'a. {list2[list1[3]]}',end='')
            print('b. int','\nc. dict',"\nd. tuple")
            answer=input("Your Answer : ")
            if(answer=='a'):
                print("Right Answer!!!You won Rs.100,000")
                print("-----------------------Next Question for Rs.200,000---------------------------")
                print(list1[4])
                print("a. [3, 4, 5, 20, 5, 25, 1, 3]","\nb.",list2[list1[4]],'\nc. [1, 3, 4, 5, 20, 5, 25]',"\nd. [1, 3, 3, 4, 5, 5, 20, 25]")
                answer=input("Your Answer : ")
                if(answer=='b'):
                    print("Right Answer!!!You won Rs.200,000")
                    print("-----------------------checkpoint Question for Rs.500,000---------------------------")
                    #print("-----------------------Next Question---------------------------")
                    print(list1[5])
                    print("a. class inside function")
                    print('b. function inside function',f'\nc. {list2[list1[5]]}',"\nd. function")
                    answer=input("Your Answer : ")
                    if(answer=='c'):
                        print("Right Answer!!!You won Rs.500,000")
                        print("-----------------------Next Question for Rs.1,000,000---------------------------")
                        print(list1[6])
                        print("a. a","\nb.",list2[list1[6]],end='')
                        print('c. B',"\nd. ~a")
                        answer=input("Your Answer : ")
                        if(answer=='b'):
                            print("Right Answer!!!You won Rs.1,000,000")
                            print("-----------------------Next Question for Rs.2,000,000---------------------------")
                            print(list1[7])
                            print("a.",list2[list1[7]],"\nb. \'a\',\'b\',\'c\',\'d\'","\nc. None","\nd. error")
                            answer=input("Your Answer : ")
                            if(answer=='a'):
                                print("Right Answer!!!You won Rs.2,000,000")
                                print("-----------------------Next Question for Rs.5,000,000---------------------------")
                                print(list1[8])
                                print("a.",list2[list1[8]],"\nb. 0",'\nc. type \'int\'',"\nd. Error")
                                answer=input("Your Answer : ")
                                if(answer=='a'):
                                    print("Right Answer!!!You won Rs.5,000,000")
                                    print("-----------------------Winning Question for Rs.10,000,000---------------------------")
                                    print(list1[9])
                                    print("a. print is keyword and return is function","\nb. print is keyword and return is also keyword ","\nc. print stores value and return shows value","\nd.",list2[list1[9]])
                                    answer=input("Your Answer : ")
                                    if(answer=='d'):
                                        print("Right Answer!!!You won Rs.10,000,000 & full Game")
                                    else:
                                        print("Wrong Answer!!!\n You Won 500,000")   
                                else:
                                    print("Wrong Answer!!!\n You Won 500,000")
                            else:
                                print("Wrong Answer!!!\n You Won 500,000")
                        else:
                            print("Wrong Answer!!!\n You Won 500,000") 
                    else:
                        print("Wrong Answer!!!\n You Won 50,000")   
                else:
                    print("Wrong Answer!!!\n You Won 50,000")
            else:
                print("Wrong Answer!!!\n You Won 50,000")
        else:
            print("Wrong Answer!!!\n You Won nothing")
            
    else:
        print("Wrong Answer!!!\n You Won Nothing")
else:
    print("Wrong Answer!!!\n You Won Nothing")
   

   

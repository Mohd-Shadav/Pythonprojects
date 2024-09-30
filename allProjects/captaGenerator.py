import random
import string

def captcha():

    captchaString = string.ascii_letters + string.digits + string.ascii_letters 
    
    captchaLength = 6

    captchaString = ''.join(random.choice(captchaString) for _ in range(captchaLength))

    return captchaString


if __name__ == "__main__":
    captchaDisplay = captcha()
    print("Your captcha is : ",captchaDisplay)
    userInput = input("Enter Captcha here : ")
    if(captchaDisplay==userInput):
        print("correct captcha✅")
    else:
        print("wrong captcha❌")

        

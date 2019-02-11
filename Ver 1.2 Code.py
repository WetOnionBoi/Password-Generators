import random
from random import randint
from string import printable
def main():
    password = ""
    num = 0
    passList = []
    passLength = int(input("How long do you want your password to be?"))
    loopAmount = passLength
    while passLength != 0:
        passChar = randint(1,10)
        if passChar > 5:
            passChar = random.choice(printable)
            passList.append(passChar)
        else:
            passChar = randint(0,9)
            passList.append(str(passChar))
        
        passLength = passLength - 1
        
    
    while num != loopAmount:
        password = password + passList[num]
        num = num + 1
    
        
    print("Your password is,", password)
    
main()
        
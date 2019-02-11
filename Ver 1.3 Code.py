import random
from random import randint           # Imported randint and printable so that I can get random numbers/letters/symbols
from string import printable
def main():
    password = ""     
    num = 0
    passList = []      # List for random numbers/letters/symbols to be appended to
    passLength = int(input("How many characters long do you want your password to be?"))           # Asks user how long many characters long they want their password to be
    loopAmount = passLength
    while passLength != 0:                                     
        passChar = randint(1,10)                               # Creates 50/50 chance for a symbol/letter to be printed or a number
        if passChar > 5:
            passChar = random.choice(printable)              # If number is less then 5 then gives a random symbol/letter
            passList.append(passChar)
        else:
            passChar = randint(0,9)                        # If the number is greater then 5 then gives random numbers between 0 - 9
            passList.append(str(passChar))
        
        passLength = passLength - 1
        
    
    while num != loopAmount:                        # Converts from list to string
        password = password + passList[num]
        num = num + 1
    
        
    print("Your password is,", password)         # Prints users password
    
main()
        
# A program that display a list of options to the user to choose from.
# 11-28-2022
# CTI-110 P5HW2 - Math Quiz
# Rana
#
import random
print("Welcome to Math Quiz\n\n")
def addRandom(): 
    n1 = random.randint(0, 100)
    n2 = random.randint(0,100) 
    print(f"  {n1}")
    print(f"+ {n2}") 
    print("Enter answer.")
    ans = int(input()) 
    guesses = 1
    while ans != n1+n2:
        if ans < n1+n2:
            print("Sorry, guess is too low. \n")
        else:
            print("sorry, guess is too high. \n")
        ans = int(input("try again: ")) 
        guesses += 1
    print("congratulations!!!! your answer is correct..")
    print(f"Number of guesses: {guesses}\n")
    
def subRandom(): 
    n1 = random.randint(0, 100)
    n2 = random.randint(0,100) 
    print(f"{n1}")
    print(f"-{n2}") 
    print("Enter answer.")
    ans = int(input()) 
    guesses = 1
    while ans != n1-n2:
        if ans < n1-n2:
            print("Sorry, guess is too low. \n")
        else:
            print("sorry, guess is too high. \n")
        ans = int(input("try again: ")) 
        guesses += 1
    print("congratulations!!!! your answer is correct..")
    print(f"Number of guesses: {guesses}\n")

if __name__ == "__main__":
    while 1:
        print("MAIN MENU")
        print("-------------")
        print("1) Adding Random Numbers ") 
        print("2) Subtracting Random Numbers")
        print("3) Exit\n") 
        num = int(input("Please choose one of the option:"))
        if num == 3:
            print("Thank you for playing...")
            print("Bye!!")
            break
        if num == 1:
            addRandom() 
        if num == 2:
            subRandom()
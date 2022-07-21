#Number Guessing Game in Python

from calendar import c
import random
import math

#generating randon number and printing the rules
x = random.randint(0, 100)
score = 100
print("\t\t\t\t\t********** Rules **********")
print("\t\t\t\t     The number is between 0 and 100.")
print("\t\t\t  You've only maximum of 7 chances to guess the integer!")
print("\t\t\t\t    You cannot exit the game once begun.")
print("\t\t\t\t You can guess the number in form of integer.")
print("\n")

#calculating hints
multiples = [x*3, x*5, x*7]
greater = x+10
less = x-10
if x > 1:
    for i in range(2, int(x/2)+1):
        if (x % i) == 0:
            prime = "It is not a prime number"
            break
        else:
            prime = "It is a prime number"
factors=[]
def get_factors(x):
    factors.clear()
    for i in range(1, int(x/2)):
       if x % i == 0:
        factors.append(i)
    if x>10:
        factors.remove(1)



#defining hints functions
def hint1():
    print("### Hint 1 ###")
    print("Multiples of number are :", multiples)
    print("\n")
def hint2():
    print("### Hint 2 ###")
    print("Number is greater than :", less)
    print("\n")
def hint3():
    print("### Hint 3 ###")
    print("Number is less than :", greater)
    print("\n")
def hint4():
    print("### Hint 4 ###")
    print(prime)
    print("\n")
def hint5():
    print("### Hint 5 ###")
    if prime == "It is not a prime number":
        get_factors(x)
        print("Its some factors are:", factors)
        print("\n")


#function to show hints
def show_hints(x, i, y):
    if x!=y and i ==1:
        hint1()
    if x!=y and i ==2:
        hint2()
    if x!=y and i ==3:
        hint3()
    if x!=y and i ==4:
        hint4()
    if x!=y and i ==5:
        hint5()


#checking the guesses
for i in range(7):
    print("\n")
    print("This is your ", i + 1, " try.")
    print("\n")
    if i > 0 and i < 6:
        show_hints(x, i, y)
    try:
        y = int(input("Guess a number:- "))
    except ValueError:
        print("The input was not a valid integer.")
    
    if x == y:
        print("\n")
        print("***** Congratulations you did it in ", i + 1, " try ******")
        print("Your score is:", score)
        print("Thanks for playing!")
        print("\n")
        break
    if x > y+20:
        print("You guessed too small!")
        score -= 10
    if x < y-20:
        print("You Guessed too high!")
        score -= 10
    if x>y and x < y+10:
            print("You guessed very close! Just a little bit higher!")
            score -= 10
    if x<y and x > y-10:
            print("You guessed very close! Just a little bit lower!")
            score -= 10



if y!=x:
    print("\n\n")
    print("You failed to guess the number in 7 tries. The number was ", x)
    print("Your score is:", score)
    print("Better luck next time!")
    print("Thanks for playing!")
    print("\n")

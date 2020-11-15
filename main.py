# Made by Pranshu Aggarwal

# Number Guessing game


import random

print("Welcome to the Number guessing game")
print("The number can be present anywhere between 2 to 1000")


print("You get +10 for correct guess and -2 for each hint that you get")

print("Your score = 0")

score = 0

def game():
    n = random.randint(2,1000)
    hint = []
    for i in range(2,n):
        if n%i==0:
            hint.append(i)
    x = int(input("Enter your guess"))

    global score
    if x == n:
        score+=10
        print("Correct")
    else:
        while x!=n:
            if len(hint)==0:
                print("It is a prime number")
                score-=2
                x = int(input("Enter your next guess"))
            else:
                j = random.choice(hint)
                score-=2
                print("One of the factors is",j)
                hint.remove(j)
                x = int(input("Enter your next guess"))
            if len(hint)==0:
                break
        score+=10
        print("Correct")
    print("Your score is",score)

p = int(input("Enter the number of times you want to play the game"))
for i in range(p):
    game()
        

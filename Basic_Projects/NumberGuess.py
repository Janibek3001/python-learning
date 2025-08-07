import random

def Validator():
    Guess = random.randint(0, 100)
    number = 0
    attempts = 0
    
    while True:
        number = int(input())
        attempts += 1
        if GuessFunction(number, Guess) == 0:
            print(f"You find it in {attempts} attempts")
            break     
        
def GuessFunction(number, guess):
    if number < guess:
        print("Too Low!")
        return 1
    elif number > guess:
        print("Too high")
        return 1
    else:
        print("You won!")
        return 0
    
Validator()
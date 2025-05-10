# Welcome to number guessing game!
import random
print("Welcome to number guessing game!")
print("I'm thinking of a number between 1 and 100.")
choice=input("Choose a difficulty. Type 'easy' or 'hard': ")
number=random.randint(1,100)
user_input=int(input("Make a guess: "))
if choice=="easy":
    attempts=10
else:
    attempts=5
    
game_over=False
while not game_over:
    if user_input==number:
        print(f"You got it! The answer was {number}.")
        game_over=True
    elif user_input<number:
        print("Too low.")
        attempts-=1
        print(f"You have {attempts} attempts remaining to guess the number.")
        if attempts==0:
            print("You've run out of guesses, you lose.")
            game_over=True
            break
        user_input=int(input("Make a guess: "))
    else:
        print("Too high.")
        attempts-=1
        print(f"You have {attempts} attempts remaining to guess the number.")
        if attempts==0:
            print("You've run out of guesses, you lose.")
            game_over=True
            break
        user_input=int(input("Make a guess: "))   
        
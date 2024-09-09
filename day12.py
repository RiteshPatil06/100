#import random 
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#check if the actual answer matches with the guess
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You guessed it correct! the answer was {actual_answer}.")        


#function to choose difficulty
def set_difficulty():
    level = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS
    else:
        print("Invalid Input. Try again")

#choice a random number between 1 and 100
def game():
    print("Welcome to the Number guessing game!")
    print("I'm thinking of a number between 0 to 100.")
    answer = random.randint(1, 100)
    print(f"Answer is {answer}")
    
    turns = set_difficulty()
    
    #make user to guess
    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of turns. Game over!")
            return
        elif guess != answer:
            print("Guess again.")

game()




 
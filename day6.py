#Hangman game
import random
from day6_hangman_art import stages, logo
from day6_hangman_words import word_list


# start of game
print(logo)

#Guessing a random word
the_word = random.choice(word_list)
print(the_word)

#replacing the word with the _
placeholder = ''
word_length = len(the_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

#rules of games
game_over = False
correct_word = []
lives = 6

#logic of game
while not game_over:
    #guess the letter
    print(f"**************************************< {lives} Lives Left >**************************************")
    guess = input("Guess the letter:").lower()

    if guess in correct_word:
            print(f"You have already guessed the letter {guess}. Guess another one...")
            

    display = ''
    
    for letter in the_word:
        if letter == guess:
            #print(f"You guessed it correct! {guess} is there. Guess another one...")
            display += letter
            correct_word.append(guess)
        elif letter in correct_word:
            display += letter    
        else:
           display += "_"

    print(display) 

    if guess not in the_word:
        print("Incorrect guess, you lose a life")
        lives -= 1
        if lives == 0:
            print("*************** Game Over, you lost ***************")
            game_over = True


    if "_" not in display:
        game_over = True
        print("*************** You win! ***************")

    print(stages[lives])    

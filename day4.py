import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
sissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game = [rock, paper, sissor]
print("Welcome to rock paper sissor!")
user_choice = int(input("What you want to choose: rock(0); paper(1); sissor(2):\n"))
print(game[user_choice])
computer_choice = random.randint(a=0 , b=2)
print("Computer choices:")
print(game[computer_choice])

if user_choice >= 3 or user_choice < 0 :
    print("Invalid input")
elif user_choice == computer_choice:
    print("It's a Draw...")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")    
elif user_choice == 1 and computer_choice == 2:
    print("You lose!!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!!")    
elif user_choice == 1 and computer_choice == 0:
    print("You win!!")    

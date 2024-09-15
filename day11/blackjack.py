import random


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

game = True
while game:
    ready = input("Wanna play blakjack game (yes/no): ")
    if ready.lower() != "yes":
        print("okay, maybe next time!")
        game =False
    else:
        #logo
        print(logo)
        #define the set of card
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]
        #give two random cards to user 
        user_card1 = random.choice(cards)
        user_card2 = random.choice(cards)
        user = [user_card1, user_card2]
        print(f"Your cards: {user}, current score: ", sum(user))
        #give two cards to computer but hide one
        computer_card1 = random.choice(cards)
        computer_card2 = random.choice(cards)
        computer = [computer_card1]
        print(f"Computer's first card: {computer}, current score: ", sum(computer))
        #ask user to hit or stand
        if sum(user) > 21: 
            print("*********************************************************************")
            print("************ You went bust. You lose!😭 ************")
            print("\n" * 20)
            break
            
        while True:
            hit = input("Type 'hit' to get another card, type 'stand' to pass: ")
            #if user hit, give another card to user and check if user bust or not
            if hit.lower() == "hit":
                user_card3 = random.choice(cards)
                user.append(user_card3)
                print(f"Your cards: {user}, current score: ", sum(user))
                computer = [computer_card1, computer_card2]
                if sum(user) > 21 and sum(computer) <= 21:
                    print("*********************************************************************")
                    print(f"Your final hand: {user} and your final score: {sum(user)}")
                    print(f"Computer's final hand: {computer} and it's final score is: {sum(computer)}")
                    print("************ You went bust. You lose!😭 ************")
                    print("\n" * 20)
                    break
            #if user stand, compare the cards of user and computer, if user win, user win    
            elif hit.lower() == "stand":
                while sum(computer) <= 18:
                    comp_card = random.choice(cards)   
                    computer.append(comp_card)
                    print(f"Computer's hand: {computer}, current score: ", sum(computer))
                if sum(user) <= 21 and sum(computer) > 21:
                    print("*********************************************************************")
                    print(f"Your final hand: {user} and your final score: {sum(user)}")
                    print(f"Computer's final hand: {computer} and it's final score is: {sum(computer)}")
                    print("************ computer went bust. You win! BLACKJACK🤑 ************")
                    print("\n" * 20)
                    break
                elif sum(user) > sum(computer):
                    print("*********************************************************************")
                    print(f"Your final hand: {user} and your final score: {sum(user)}")
                    print(f"Computer's final hand: {computer} and it's final score is: {sum(computer)}")
                    print("************ You win! BLACKJACK🤑 ************")
                    print("\n" * 20)
                    break
                elif sum(user) < sum(computer):
                    print("*********************************************************************")
                    print(f"Your final hand: {user} and your final score: {sum(user)}")
                    print(f"Computer's final hand: {computer} and it's final score is: {sum(computer)}")
                    print("************ You lose!😭 ************")
                    print("\n" * 20)
                    break
                elif sum(user) == sum(computer):
                    print("*********************************************************************")
                    print(f"Your final hand: {user} and your final score: {sum(user)}")
                    print(f"Computer's final hand: {computer} and it's final score is: {sum(computer)}")
                    print("************ It's a Draw!🫠  ************")
                    print("\n" * 20)
                    break


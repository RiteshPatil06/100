#Find the treasure game

print("Welcome to the treasure island.\nYour mission is to find the treasure")
print("You are standing on the entrance of the cave and have two ways(Left or Right), which way you want to go?: ")
LorR = input()
start = LorR.lower()
while True:
    if (start == 'left'):
        print("You have entered the cave and now theres a river infront of you.")
        print("Would you like to swim(type: swim) or wait(type: wait)?")
        river = input()
        if(river == 'wait'):
            print("Excellent! You got saved from those crocodiles...")
            print("Ohh! there are three doors opened in wall (red, white, and blue)")
            door = input("Which door you think will lead to treasure?:\n")
            if(door == 'red'):
                print("There was fire inside, you die! Game over!")
                break
            elif(door == 'white'):
                print("There was a Polar bear inside, you die! Game over!")
                break
            elif(door == 'blue'):
                print("Hurray! You found the treasure.")
                break
            else:
                print("Invalid choice, Game over!")
                break
        elif(river == 'swim'):
            print("You got eaten by crocodiles... Game over!")
            break
        else:
            print("Invalid choice, Game over!")
            break
    elif(start == 'right'):
        print("You entered the hungry lions den... Game over!")
        break
    else:
        print("Invalid choice, Game over!")
        break
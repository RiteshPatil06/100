#auction

def find_higest_bid(biding_dictionary) :
    winner = ""
    highest_bid = 0

    for bidder in the_list:
        bid_amount = the_list[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")        

the_list = {}
continue_biding = True
while continue_biding: 
    print("Welcome bidder to the auction ;>")
    name = input("Name of the the bidder: ")
    bid = int(input("Price for the bid: "))
    the_list[name] = bid  
    ask = input("Is there any other bid to be placed?(yes/no)\n")

    if ask == 'yes':
        print("\n" * 20)

    elif ask == 'no':
        find_higest_bid(bid)
        continue_biding = False   
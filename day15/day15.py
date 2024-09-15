MENU = {
    "espresso": {
        "ingridents": {
            "water" : 50,
            "coffee" : 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingridents": {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingridents": {
            "water" : 250,
            "milk" : 50,
            "coffee" : 24,
        },
        "cost": 3.0
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
    "money": 0
}





#if user says 'off' so quit
def order_off():
    print("Thanks for visiting! See you soon...")
    return

#function to print report of resources
def order_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}gm")
    print(f"Money: ${round(resources['money'], 2)}")
    
#function to check resources are sufficent
def is_resource_sufficient(order):
    for item in MENU[order]["ingridents"]:
        if MENU[order]["ingridents"][item] > resources[item]:
            print(f"Sorry! Not enough {item} to make your {order}😭😭.")
            print("Come back later...")
            return False
    return True

#function to cal money and process coins
def process_coins():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    print('Please insert coins.')
    quarters_amt = int(input("How many quarters: "))
    dimes_amt = int(input("How many dimes: "))
    nickles_amt = int(input("How many nickles: "))
    pennies_amt = int(input("How many pennies: "))
    total_amt = (quarters * quarters_amt) + (dimes * dimes_amt) + (nickles * nickles_amt) + (pennies * pennies_amt)
    required_amount = MENU[order]["cost"]
    return total_amt, required_amount

#function to check transaction successful?
def check_transaction():
    total_amt, required_amount = process_coins()
    if total_amt < required_amount:
        print("Sorry! not enough money for a coffee.😐")
        return
    else:
        print(f"Here is your {order}☕! Enjoy!")
        remaining_amt = total_amt - required_amount
        remaining_amt = round(remaining_amt, 2)
        resources["money"] += remaining_amt
        print(f"Here's your change of ${remaining_amt}")
        
#function to make coffee
def make_coffee():
    if order == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
    elif order == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
    elif order == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 50
        resources["coffee"] -= 24
        
        
coffee_machine = True
money = 0        

while coffee_machine:
    #print(espresso/latte/cappuccino)?
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "report":
        order_report()
    elif order == "off":
        order_off()
        coffee_machine = False
        break
    else:
            if not is_resource_sufficient(order):
                break
            check_transaction()
            make_coffee()        
        
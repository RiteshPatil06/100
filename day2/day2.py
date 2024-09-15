#Tip Calculator

print("Welcome to the Tip Calculator.")
total = int(input("What was the total bill?: "))
tip = int(input("How much would you like to tip?: "))
split = int(input("How many people to split the bill?: "))
per_person = (total + tip) / split
print(f"Per person has to pay: {per_person}")
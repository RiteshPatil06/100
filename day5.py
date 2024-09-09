#password generator
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!','@','#','$','%','&','*','(',')','?','/','-']

nr_letter = int(input(f"How many letters you want in password?\n"))
nr_number = int(input(f"How many numbers you want in password?\n"))
nr_symbol = int(input(f"How many symbols you want in password?\n"))
password = []
for char in range(0, nr_letter):
    password.append(random.choice(letters))
for char in range(0, nr_number):
    password.append(random.choice(number))
for char in range(0, nr_symbol):
    password.append(random.choice(symbol)) 
random.shuffle(password) 

new_password = ''
for char in password:
    new_password += char
print(new_password)         
    
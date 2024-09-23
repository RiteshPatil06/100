#try catch except finally method

# try:
#     file = open("a_file.txt") #filenotfound error
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["dfdfd"]) #KeyError
# except FileNotFoundError:
#     file = open("a_file.txt", 'w')
#     file.write("something")
# except KeyError as error_msg:
#     print(f"The key {error_msg} was not found.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("The file has been closed.")


fruits = ["Apple", "Pear", "Orange"]


# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

try:
    make_pie(2)
except IndexError:
    print("Fruit Pie")



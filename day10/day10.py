#Calculator

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    should_accumulate = True
    num1 = float(input("What's your first number: "))

    while should_accumulate:
        for operation in operations:
            print(operation)
        user_operation = input("Pick an operation: ")
        num2 = float(input("What's your second number: "))  
        answer = operations[user_operation](num1, num2)
        print(f"{num1} {user_operation} {num2} = {answer}")
        choice = input("Type 'y' to continue with the previous answer or,\nType 'n' to start new calculation or,\nType 'q' to end the program: " )

        if choice.lower() == 'y':
            num1 = answer
        elif choice.lower() == 'q':
            break    
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()            
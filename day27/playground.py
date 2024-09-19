def add(*args):
    print(type(args))
    print(args)
    return sum(args)

print(add(1,2,3,4,10,50))

def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=10, multiply=5)
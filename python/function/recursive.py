def factorial(x):
    if x == 1:
        return x
    else:
        return (x * factorial(x-1))
x = int(input('Int : '))
print(f'Factorial of {x} is {factorial(x)}')
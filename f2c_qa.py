# exercise 4.1
f = eval(input('temperature fahrenheit:'))


def celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


print(f'{f} degrees fahrenheit is equivalent to {celsius(f):0.3} degrees in celsius.')

# exercise 4.5
import sys

try:
    fahrenheit = float(sys.argv[1])
except IndexError:
    print(f'no fahrenheit value entered')
    sys.exit(1)



def celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


print(f'{f} degrees fahrenheit is equivalent to {celsius(f):0.3} degrees in celsius.')


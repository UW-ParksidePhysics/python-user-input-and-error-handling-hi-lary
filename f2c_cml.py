# exercise 4.2
"""exercise 4.1 but fahrenheit is read from the command line"""

import sys
print(float(sys.argv[1]))

f = eval(input('temperature fahrenheit:'))


def celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


print(f'{f} degrees fahrenheit is equivalent to {celsius(f):0.3} degrees in celsius.')


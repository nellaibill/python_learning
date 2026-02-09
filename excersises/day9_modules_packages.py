#Importing from a Package
from utilities.helpers import print_separator
#Using Built-in Modules
import math
print(math.sqrt(16))  # Output: 4.0
print(math.pi)      # Output: 3.141592653589793
print_separator()

import random
print(random.randint(1, 10))  # Output: A random integer between 1 and 10
print_separator()

import datetime
now = datetime.datetime.now()
print(now)  # Output: Current date and time
print_separator()

#Import with alias
import math as m
print(m.sqrt(25))  # Output: 5.0
print_separator()

#Import specific items

from math import sqrt,pi
print(sqrt(36))  # Output: 6.0
print(pi)       # Output: 3.141592653589793
print_separator()

#Creating Your Own Module
import calculator
print(calculator.add(5, 3))  # Output: 8
print(calculator.sub(5, 3))  # Output: 2
print_separator()

def main():
    print("This is the main function.")
print("Top Level Code: This will run when the module is imported or executed directly.")    
if __name__ == "__main__":
    main()    
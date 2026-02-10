print("Hello World!")
name ="Saleem"
age = 35
height = 5.8
is_developer = True

# Step 3: Variables & Data Types
print("My name is", name)
print("I am", age, "years old")
print("My height is", height, "feet")
print("Am I a developer?", is_developer)

#Step 4: Check Data Type

print (type(name))
print (type(age))
print (type(height))
print (type(is_developer))

#Step 5: User Input (Very Important)
name =input("What is your name? ")
age = input("what is your age? ")
print("Hello " +name+" your age is "+age)

#input() always returns a string.
print (type(age)) # This will show that age is of type string
# To convert age to an integer, we can use int()
age =int(age)
print (type(age)) # Now age is of type int

#Step 6: Simple Calculation
#I want to enter my birth year it needsto calcuate age
import datetime
birth_year = int(input("Enter your birth year: "))
current_year = datetime.datetime.now().year
age = current_year - birth_year
print("You are", age, "years old")

#Step 7: Python Comments

#This is a Single Lien Comment
"""
This is a Multi Line Comment 
It can span multiple lines

"""
#Step 8: Small practice task
#Ask the user for two numbers and print their sum
num1 = input("Enter first number: ")
num2 = input("Enter Second number: ")
num3 = int(num1)+ int(num2)
print ("The Sum of num1 and num2 is",num3)


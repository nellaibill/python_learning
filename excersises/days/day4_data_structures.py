#List
from asyncio import Task


numbers =[1, 2, 3, 4, 5,5,4]
print(numbers) # Output: [1, 2, 3, 4, 5,5,4]
names=["Alice", "Bob", "Charlie"]
print(names) # Output: ["Alice", "Bob", "Charlie"]
print("-------------------------------")
#Access & Modify
print(numbers[0])
numbers[0] = 20
print(numbers) # Output: [1, 20, 3, 4, 5]
print("-------------------------------")

#Common List Operations

# Append
numbers.append(6)
numbers.insert(2, 30) # Insert 20 at index 1
numbers.remove(20) # Remove the first occurrence of 20
print(numbers) # Output: [1, 20, 30, 3, 4, 5, 6]

print("-------------------------------")

#Tuple (Read-Only List) 
coordinates = (10,20)
print(coordinates) # Output: (10, 20)
print(coordinates[0]) # Output:
#coordinates[0] = 30 # This will raise an error because tuples are immutable

#How to identify tuples?
# Tuples are defined using parentheses () and cannot be modified after creation.

print("-------------------------------")

#Set
#Sets are best for removing duplicates.
unique_numbers = {1, 2, 3, 4, 5,1,2,8}
print(unique_numbers) # Output: {1, 2, 3, 4, 5, 8}

print("-------------------------------")

#Dictionary (Key-Value Pairs)

person ={
    "name": "Alice",
    "age": 30,
}

print(person) # Output: {'name': 'Alice', 'age': 30}
print (person["name"]) # Output: Alice
print (person["age"]) # Output: 30

print("-------------------------------")
person["age"] = 31
print(person) # Output: {'name': 'Alice', 'age': 31}

#Loop Through Dictionary (Interview Favorite)

for key in person:
    print(key, ":", person[key])

print("-------------------------------")

"""
Task 1

Create a list of 5 numbers

Print only even numbers
"""
numbers =[1,2,3,4,5,6,7,8,9,10]
for num in numbers:
     if(num%2==0):
            print(num)
            
print("-------------------------------")           

"""
Task 2

Create a tuple of 3 cities

Try modifying it (see error)
"""

cities=("salem","nellai","karur")

print(cities) # Output: ('salem', 'nellai', 'karur')
#cities[0]   ="tuticorin" # This will raise an error because tuples are immutable

print("-------------------------------")

"""
Task 3

Remove duplicates from a list using set
"""

numbers ={1,2,3,4,5,12,2,3}
print(numbers) # Output: {1, 2, 3, 4, 5, 12}

print("-------------------------------")

"""
Task 4

Task 4

Create a dictionary for employee details

Loop and print all keys and values

"""

employee = {
    "name":"John Doe",
    "age": 28,
    "position": "Software Engineer"
}
for key in employee:
    print(key + ":", employee[key])
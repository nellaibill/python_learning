def print_separator():
    print("--------------------------------")
         
name ="saleem"
city="tirunelveli"
print(name)
print(name[0])
print_separator() 
#String Slicing
print(name[0:3]) # Output: sal
print(name[:3]) # Output: sal
print(name[3:]) # Output: eem
print(name[::-1]) # Output: meelas
print_separator()

#String Immutability
#name[0] = "S" # This will raise an error because strings are immutable  

#Common String Methods
print(name.upper()) # Output: SALEEM
print(name.lower()) # Output: saleem
print(name.capitalize()) # Output: Saleem
print("  Hello World   ".strip()) # Output: Hello World (removes leading/trailing whitespace)
print(name.replace("e", "a")) # Output: salaam
print_separator()

#split() and join()
data="apple,banana,orange"
fruits=data.split(",") # Output: ['apple', 'banana', 'orange']
print(fruits)
print_separator()
words=["Hello", "World"]
sentence=" ".join(words) # Output: Hello World
print(sentence)
print_separator()

#String Formatting
print(f"my name is {name} and I live in {city}") # Output: my name is saleem and I live in tirunelveli
print("my name is", name, "and I live in", city) # Output: my name is saleem and I live in tirunelveli

#Check Substring
text ="python programming"
print("python" in text) # Output: True
print("python" not in text) # Output: False
print_separator()
#Loop Through String

for char in name:
    print(char)
    
print_separator()    


#Task 1 Reverse a string without using built-in reverse

reverse_name = ""
for char in name:
    print(char)
    reverse_name = char + reverse_name
    print(reverse_name)
print("Reversed name is", reverse_name)
print(name[::-1])

#Task 2 Count number of vowels in a string
vowels = "aeiouAEIOU"
count = 0
for char in name:
    if char in vowels:
        count += 1
print("Number of vowels in", name, "is", count) # Output: Number of vowels in saleem is 3
print_separator()

# Task 3 Check if a string is a palindrome

text ="mama"
text2=text[::-1]
if text == text2:
    print("Palindrome")
else:
    print("Not a Palindrome")    
    
#Task 4 Format a sentence using f-string    
name="saleem"
age=25
print(f"My name is {name} and I am {age} years old") # Output: My name is saleem and I am 25 years old
def functon_name(parameters):
    # function body
    # code to be executed
    return result  # optional, can return a value or nothing    

#Example Function: Greet User
def greet(name):
     print("Hello", name)
   
def print_separator():
    print("--------------------------------")
         
             
greet("Alice") # Output: Hello Alice
greet("Bob") # Output: Hello Bob    
print_separator() # Output: --------------------------------     

#Function With Return Value
     
def sum_numbers(num1,num2):
    return num1+num2;

result=sum_numbers(1,2)
print("The sum is",result) # Output: The sum is 3

print_separator() # Output: --------------------------------
#Default Parameters

def greet(name="Guest"):
    print("Hello", name)
    
greet() # Output: Hello Guest
greet("Alice") # Output: Hello Alice    
print_separator() # Output: --------------------------------

#Multiple Return Values

def calculate(a,b):
    addition = a+b
    multiply = a*b
    return addition, multiply

add, mul = calculate(25,10)
print("Addition:", add) # Output: Addition: 35
print("Multiplication:", mul) # Output: Multiplication: 250

print_separator() # Output: --------------------------------

#Function Calling Another Function

def calculate_total(price, quantity):
    return sum_numbers(price, quantity)

print("Total:", calculate_total(100, 2)) # Output: Total: 102
print_separator() # Output: --------------------------------

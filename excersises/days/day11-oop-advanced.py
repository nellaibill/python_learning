#OOP Advanced
#Inheritance
from utilities.helpers import print_separator
class Person:
    def __init__(self,name):
        self.name = name
        
    def greet(self):
        print(f"Hello, I am {self.name}")
        
    def role(self):
        print("I am a person")  
        
         
        
class Employee(Person):
    def __init__(self,name,employee_id):
        super().__init__(name)
        self.employee_id = employee_id
        
    def show_employee_id(self):
        print(f"My employee ID is {self.employee_id}")
        
    def role(self):
        print("I am an employee")  
      
        
e = Employee("Saleem",12345)
e.greet() # Output: Hello, I am Saleem
e.show_employee_id() # Output: My employee ID is 12345   
print_separator() 
#Method Overriding         
e.role() # Output: I am an employee
print_separator() 
#Polymorphism

class Dog:
    def speak(self):
        print("Woof!")
       
class Cat:
    def speak(self):
        print("Meow!")

def animal_sound(animal):                
    animal.speak()
dog = Dog()
cat = Cat()
animal_sound(dog) # Output: Woof!
animal_sound(cat) # Output: Meow!
print_separator()
#Encapsulation
class Account:
    def __init__(self,account_number,balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance  # Private attribute
        
    def get_balance(self):
        return self.__balance
    
acc1 = Account("Account1",1000)
print(acc1.account_number) # Output: 101 (Public attribute)
print(acc1.get_balance()) # Output: 1000 (Private attribute via public method)  



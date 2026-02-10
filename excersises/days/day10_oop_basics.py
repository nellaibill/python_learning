from utilities.helpers import print_separator
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
person1 = Person("Saleem",36)
print(person1.name) # Output: Saleem
print(person1.age)  # Output: 36
print_separator()   
#Instance Methods

class Employee:
    def work(self):
        print(f"hello")
        
Employee1 = Employee()
Employee1.work() # Output: Hello
print_separator()        

#Real-Life Example

class BankAccount:
    def __init__(self,balance):
        self.balance = balance      
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")
        
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
            
account = BankAccount(1000)
account.deposit(500)  # Output: Deposited 500. New balance is 150
account.withdraw(200) # Output: Withdrew 200. New balance is 1300
account.withdraw(2000) # Output: Insufficient funds
            
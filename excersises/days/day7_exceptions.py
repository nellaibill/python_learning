#Exception Handling in Python
#print(10/0) # This will raise a ZeroDivisionError

#try / except (Basic)
try:
    print(10/0) # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
    
try:
    num = int(input("Enter a number: "))
    print(10/num)   
except ZeroDivisionError:
    print("Cannot divide by zero!")    
except ValueError:
    print("Invalid input! Please enter a valid number.")
    
#Generic Exception Handling
try:
    x=int("abc") 
    
except Exception as e:
    print("An error occurred:", e)
    
#else Block
try:
    num = int(input("Enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")

#finally Block

try:
    num = int(input("Enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This block will always execute regardless of exceptions.")            

#Real-Life Example: ATM Withdrawal

balance = 1000
withdrawal_amount = int(input("Enter withdrawal amount: "))
try:
    if withdrawal_amount > balance:
        raise ValueError("Insufficient funds!")
    else:
        balance -= withdrawal_amount
        print("Withdrawal successful! Remaining balance:", balance) 
except ValueError as e:
    print("Error:", e)    
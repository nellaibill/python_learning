#Comparison Operators
# ==, !=, >, <, >=, <=
a =10
b =20
print(a == b) # False because a is not equal to b
print(a != b) # True because a is not equal to b
print(a > b) # False because a is not greater than b
print(a < b) # True because a is less than b
print (a>=b) # False because a is not greater than or equal to b
print (a<=b) # True because a is less than or equal to b

age =int(input("Enter your age: "))
#if Statement (Basic Decision)
if age>=18:
     print("You are an adult.")

#if else Statement (Two-way Decision)
if age>=18:
      print("you can vote")
else:
      print("you cannot vote")  
      
#if elif else Statement (Multiple Decision)
if age<13:
      print ("You are  a child.")
elif  age<18:
      print ("You are a teenager.")
else:      
      print ("You are an adult.")
      
#Logical Operators
# and, or, not
# and operator
if age>=18 and age<65:
      print("You are an adult.")    

# or operator
# You can vote if you are 18 or older, or if you are a citizen
is_citizen = True
if age>=18 and  is_citizen:
      print("You can vote.")    

# not operator
# You cannot vote if you are not 18 or older'

if not age>=18:
 print("you are not eligible to vote")      

#Real-Life Example: Login System
username =input("Enter username ")
password = input("Enter Password ")
if username =="admin" and password =="password123":
      print("Login successful!")
else:
        print("Invalid username or password.")
        
#Real-Life Example: Driving License
age = int(input("Enter your age: "))
if age<18:
       print("You are not eligible for a driving license.")
elif age>=18 and age <60:
            print("You are eligible for a driving license")
else:
      print("You are  eligible for a driving license, but you should get a medical checkup.")
      
#Task 1: Even or Odd

num1 = 20
if(num1 %2 ==0):
    print("Even")
else:
      print("Odd")      
      
#Task 2: Positive, Negative, or Zero 
if num1==0:
      print("Zero")
elif num1>0:
      print("Positive")
else:
      print("Negative")
      
#Task 3: Simple ATM Check

balance =5000

withdraw=int(input("enter withdraw amount"))
if(withdraw <=balance):
 print ("please collect your cash")
 remaining_balance =balance-withdraw
 print("remaining balance",remaining_balance)
else:
 print ("No sufficient account balance")
          
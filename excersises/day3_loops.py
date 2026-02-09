#Why Do We Need Loops?
#Loops are used to repeat a block of code multiple times. They are useful when you want to perform the same action on a collection of items, or when you want to repeat an action until a certain condition is met.
print("-------------------------------")
print("1")
print("2")
print("3")
print("-------------------------------")

#Without loops, we would have to write the same code multiple times, which is inefficient and can lead to errors. Loops allow us to write cleaner and more efficient code.

for i in range(1, 4):
    print(i)
print("-------------------------------")    
for i in range(5):
        print(i)            
print("-------------------------------")       

#range() Function (Important)
# The range() function is used to generate a sequence of numbers. It takes three parameters: start, stop, and step. The start parameter is the starting number of the sequence, the stop parameter is the ending number of the sequence (exclusive), and the step parameter is the increment between each number in the sequence.

print(list(range(5))) # Output: [0, 1, 2, 3, 4]
print(list(range(1, 6))) # Output: [1, 2,
print(list(range(1,10,2))) # Output: [1, 3, 5, 7, 9]
print("-------------------------------")       
#Loop Through a List
fruits =["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
print("-------------------------------")       
#Real-Life Example: Sum of Numbers
total =0
for i in range(1,6):
 total = total+i
 
print ("Total is",total)    
print("-------------------------------")       
#while Loop (Condition-Based Loop)
count =1
while count<=5:
    print(count)
    count = count+1
print("-------------------------------")        
 #break Statement 
count =0;
while True:
     if count ==3:
         break
     count = count+1
     print(count)
print("-------------------------------")               

#continue Statement
for i in range(1,10):
 if(i==6):
      continue
 print(i)
print("-------------------------------")
 
#Real-Life Example: Password Attempts

attempts =0;
max_attempts =3;

while attempts <max_attempts:
    password =input("Enter password ")
    if(password == "123"):
      print("successful")
      break
    else:
      attempts += 1
      print ("retry again")
else:
  print ("Account locked")
print("-------------------------------")
#Task 1: Print Even Numbers (1–20)
for i in range(1,21):
     if(i%2==0):
         print(i)
         
print("-------------------------------")         
#Task 2: Multiplication Table
num = int((input("Enter a number to display its multiplication table: ")))
for i in range(1,11):
     print(i,"*",num,"=", i*num)     

print("-------------------------------")     
#Task 3: Reverse Counting   
for i in range(10,0,-1):
    print(i)  
    
print("-------------------------------")    
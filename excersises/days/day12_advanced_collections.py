from utilities.helpers import print_separator
#Normal loop vs List Comprehension
#Normal loop
squares=[]
for i in range(1,6):
     squares.append(i*i)

print(squares) 
print_separator()    

#List Comprehension
#[expression for item in iterable]
squares = [i*i for i in range(1,6)]
print(squares)
print_separator()

#With condition

squares =[i*i for i in range(1,11) if i%2 ==0]
print(squares)
print_separator()


#Dictionary Comprehension

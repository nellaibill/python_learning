from utilities.helpers import print_separator
# Built-in Functions & Utilities
#lambda

add = lambda a,b : a+b
print(add(2,3)) 
print_separator()
#map
numbers = [1,2,3,4,5]
squares = list(map(lambda x:x*x,numbers))

print(squares)
print_separator()

#filter

numbers = [1,2,3,4,5]
even = list(filter(lambda x:x%2 ==0,numbers))
print(even)
print_separator()

#sort

numbers =[6,8,1,2,3,4,5]
print(sorted(numbers))
print_separator()
print(all(n>4 for n in numbers))
print_separator()
print(any(n>4 for n in numbers))
print_separator()







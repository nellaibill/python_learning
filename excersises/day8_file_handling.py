#Writing to a File
file = open("sample.txt", "w")
file.write("Hello, this is a sample file.\n")
file.write("It contains multiple lines of text.\n")
file.close()
#Reading from a file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
#Appending to a file
file = open("sample.txt", "a")
file.write("This line is appended to the file.\n")
file.close()
#Reading the updated file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
#Overwriting a file
file = open("sample.txt", "w")
file.write("This file has been overwritten.\n")
file.close()
#Reading the overwritten file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

#with Statement


#Handling File Not Found Error
try:
    with open("sample1.txt","r") as file:
        print(file.read())
        
except FileNotFoundError:
        print("The file does not exist.")
from datetime import date,datetime
from utilities.helpers import print_separator
print(date.today())
print_separator()   
#Formatting dates

now = datetime.now()
formtted =now.strftime("%d-%M-%Y")
print(formtted)
print_separator()

#Parsing String to Date
date_str= "25-01-2026"
dt = datetime.strptime(date_str,"%d-%m-%Y")
print(dt)
print_separator()

#Date Difference
d1= datetime(2025,1,1)
d2= datetime(2025,3,3)
diff =d2-d1
print(diff.days)



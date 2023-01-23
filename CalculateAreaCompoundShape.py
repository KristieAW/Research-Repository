# CalculateAreaCompoundShape.py
# Author: Kristie Warmington
# Date: 17.12.2022
# Shape consists of half a circle, a rectangle and a triagle

# getting user imput
a = int(input("Please enter the length of a\n"))
b = int(input("Please enter the length of b\n"))
c = int(input("Please enter the length of c\n"))

# working out the 3 parts
total_area = int(3.14*c**2)+(a*c)+((c*b)/2)

print("The area of your shape is ", total_area,"\n")

#Testing
'''
print("My assertions are:"
    "\na = 1, b = 3, c = 2 output = 17"
    "\na = 3, b = 6, c = 12 output = 524")
'''

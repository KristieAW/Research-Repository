# Function1.py
#
# @author: A.N.Other
# date: December 2022

def show_hello():
    print("Hello there, this is my very first function!\n\n")

print("Testing my first user defined function...\n\n")

#invoking the function
show_hello()

#invoking the function again
show_hello()

year_of_birth = int(input("Please enter your birth year "))

def your_age():
    age = 2022 - year_of_birth
    print(age)

your_age()

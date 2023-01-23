# VetPatrons.py
#
# @ Author: Kristie Warmington
# Date: 17.12.2022

from datetime import date

year_of_birth = 1993
name = input("Please input your name: ")

current_year = (date.today().year)

print("This program vets patrons before allowing them entry to the bar...\n")

# Test case assertion 1: result should be True
print("The patrons eligibility to enter the bar is ",
      str((current_year - int(year_of_birth) >= 21)
          and name != "Suzanne May"
          and name != "Wiremu Rangi"), ".")
      
name = input("\nPlease enter your full name: ")
year_of_birth = input("Please enter your year of birth: ")
                      
print("The patrons eligibility to enter the bar is ",
      str((current_year - int(year_of_birth) >= 21)
          and name != "Suzanne May"
          and name != "Wiremu Rangi"), ".")

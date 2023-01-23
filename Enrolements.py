# Enrolments.py
#
# @ author: A. N. Other
# date: September 2016

distance_from_door = 0
age_in_years = 25
print("This program vets patrons before allowing them entry to the bar...\n")

# Test case assertion 1: result should be False
print("The patrons eligibility to enter the bar is ",
      distance_from_door < 1
      and age_in_years > 20, "\n")
 
distance_from_school = 3
age_in_years = 14
has_residency = True
is_fee_foreign = False
print("This program works out eligibility for enrolment....\n")
 
# Test case assertion 1: result should be True
print("The student's eligibility to enrol is ",
      distance_from_school < 4
      and age_in_years < 18
      and has_residency
      or age_in_years < 18
      and is_fee_foreign, "\n")
 
print("The student waited for too long...\n")
age_in_years = 18
 
# Test case assertion 2: result should be False
print("The student's eligibility to enrol now is ",
      distance_from_school < 4
      and age_in_years < 18
      and has_residency
      or age_in_years < 18
      and is_fee_foreign, "\n")

print("A new student has decided to enrol.\n")

distance_from_school = 3
age_in_years = 12

# Test case assertion 3: result should be True
print("The student's eligibility to enrol now is ",
      distance_from_school < 4
      and age_in_years > 10
      and age_in_years < 18, "\n")

distance_from_school = int(input("Please enter the distance in kilometers from the school to your home , \n"))
age_in_years = int(input("Please enter your age\n"))

print("The student's eligibility to enrol now is ",
      distance_from_school < 4
      and age_in_years > 10
      and age_in_years < 18, "\n")    

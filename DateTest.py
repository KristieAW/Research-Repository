# DateTest.py
# Example of datetime and timedelta
# Date: 15.12.2022

from datetime import datetime
from datetime import timedelta

date_input = input("Please enter you DOB in the format DD Mmm YYYY: \n")

# case to a datetime object
date_object = datetime.strptime(date_input, '%d %b %Y')

# output some confirmation
print ("The year entered is ", date_object.year, "\n")

# do a calculation
my_age = datetime.today() - date_object

# show the result in different formats
print ("My exact age is ", my_age, "\n")
print ("My exact age just in days is ", my_age.days, "days\n")
print ("My exact age just in years is ", int(my_age.days/365), "years\n")

#add 10 days to my current age
print ("In 10 days time my age will be ", datetime.today() + timedelta(days=10), ".\n")

# add my current age to today's date
print ("I will be double my age in ", datetime.today() + my_age, ".\n")

my_dob = date_input

# show a date 125 days earlier then the date entered.
print ("The date 125 days before your birthday was ", datetime.today()-date_object - timedelta(days=125) ".\n")

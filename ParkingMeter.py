# ParkingMeter.py
# Example of if statement
# Date: 18.12.2022

print ("Kia Ora, this is a parking meter")
park_time = 4
print ("Park time is ", park_time, " hours. \n")


rate = 4
cost = 0
if park_time > 3:
    cost = rate *3
    # drop the rate by $2
    rate -=2
    # get the remainder of the parking time
    park_time -= 3
    # add to current cost
    cost += rate * park_time
    print("The cost of the parking is $", cost)
else:
    cost = rate * park_time
    print ("The cost of the parking is $", cost)

# test case assertion 1
'''
park_time = 4
total cost of parking = $14
'''

print ("\nKia Ora, this is a parking meter")
park_time = input("Please enter the number of hours you wish to park for: ")

# variable cast to int
park_time = int(park_time)
print ("Park time is ", park_time, " hours. \n")

rate = 4
cost = 0
if park_time > 3:
    cost = rate *3
    # drop the rate by $2
    rate -=2
    # get the remainder of the parking time
    park_time -= 3
    # add to current cost
    cost += rate * park_time
    print("The cost of the parking is $",cost)
else:
    cost = rate * park_time
    print ("The cost of the parking is $",cost)
       
# test case assertion 2
'''
park_time = 6
total cost of parking = $18
'''

# test case assertion 3
'''
park_time = 2
total cost of parking = $8
'''

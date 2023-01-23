# NewZealandFactQuiz.py
# @ Author: K A Warmington
# Example of conditional syntax
# Date: 18.12.2022

from time import time

print ("Welcome to a short quiz on interesting facts about New Zealand.")
print ("Each question will be multi choice, please select your answer by entering \nthe number 1, 2 or 3 and hit enter.")

print ("Which New Zealand town has the highest population of people that identify \nas Maori?")
print ("1. Timaru ")
print ("2. Wairoa ")
print ("3. Huntly ")

start_time = time()

x = input("Enter your answer here:" )
# cast x to int
x = int(x)

if x == 1:
    print('incorrect')
elif x == 3:
    print('incorrect')
elif x == 2:
    print('correct')
else:
    print('incorrect entry')

print ("What New Zealand city has the steepest street in the world? ")
print ("1. Dunedin ")
print ("2. Wellington ")
print ("3. Auckland ")

x = input("Enter your answer here:" )
# cast x to int
x = int(x)

if x == 1:
    print('correct')
elif x == 3:
    print('incorrect')
elif x == 2:
    print('incorrect')
else:
    print('incorrect entry')

print ("What is the Maori name for Russell? ")
print ("1. Whakatu ")
print ("2. Kororareka ")
print ("3. Tamaki Makaurau ")

x = input("Enter your answer here:" )
# cast x to int
x = int(x)

if x == 2:
    print('correct')
elif x == 3:
    print('incorrect')
elif x == 1:
    print('incorrect')
else:
    print('incorrect entry')

print ("What percentage of land is uninhabited in New Zealand ")
print ("1. 67% ")
print ("2. 91% ")
print ("3. 78% ")

x = input("Enter your answer here:" )
# cast x to int
x = int(x)

if x == 3:
    print('correct')
elif x == 2:
    print('incorrect')
elif x == 1:
    print('incorrect')
else:
    print('incorrect entry')

end_time = time()
execution_time = end_time - start_time
elapsed_time = round((execution_time / 60), 2)

print("The time it took you to complete this quiz was ", elapsed_time ,"minutes.")

input("Press the enter key to exit.")


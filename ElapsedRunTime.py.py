# ElapsedRunTime.py
# @ Author: K A Warmington
# Example of how to show the running time
# Date 18.12.2022

from time import time

start_time = time()
print("Your start time is:", start_time)

input("please enter your name, address, D.O.B, Occupation and birth place: ")

end_time = time()
print("Your end time is:", end_time)

execution_time = end_time - start_time
final_elapsed_time = round((execution_time / 60), 2)
print("Your time to complete the quiz is ", final_elapsed_time ," minutes.")



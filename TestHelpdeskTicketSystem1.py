# TestHelpdeskTicketSystem1.py
#
# @Author K W Warmington
# Date 27.12.2022

number = int(input("Enter menu selection 0-5 : "))

if number == 0:
    print("The program has been terminated, goodbye.")
    quit()

# creating and setting a ticket number
ticket_number = 2000

def assign_ticket_number(ticket_number):
    print("Ticket: {0}\n"
          .format(ticket_number + 1)

# need to find out how to repeat the below everytime someone selctes 1
# need to find out how to store the data to recall it later.

while number == 1
    ticket_number += 1
    staff_id = input(str("Enter your staff ID: "))
    staff_name = input("Enter your name: ")
    staff_email = input("Enter your email address: ")
    print("If you require a new password type: Password change ")
    ticket_issue = input("Enter the description of the problem: ")
    if ticket_issue=="Password change":
            staff_id_list = list(staff_id)
            staff_name_list = list(staff_name)
            a = ''.join(staff_id_list[:2])
            b = ''.join(staff_name_list[:3])
            print("Your ticket number is {0}.\n"
                  .format(ticket_number))
            print("Your new password is: ",(a+b))
            ticket_status = "closed"
            issue = str(input("Do you have another issue to submit? (Y/N) "))
            if issue in("y","Y","YES","yes","Yes"):
                number = 1
    else:
            ticket_status = str(open)
    # check if another ticket needs to be entered
    next_issue = input("Do you have another issue to submit? (Y/N) ")
    if next_issue=="Y":
        return option
        number = int(input("Enter menu selection 0-5 : "))
    else:
        number = 0

while number == 1:
    submitting_a_ticket()


# TestHelpdeskTicketSystem3.py
#
# Author: K.A Warmington
# Date: 09 January 2023

print("IT5016D Helpdesk Ticket System")
number = ()

# setting function to print menu options
def menu_options():
    print("------------------------------------------------------------\n"
          "Select from the following choices.\n"
          "0: Exit and end the program \n"
          "1: Submit helpdesk ticket \n"
          "2: Show all tickets \n"
          "3: Respond to ticket by number \n"
          "4: Reopen a closed ticket \n"
          "5: Display ticket status \n"
          "------------------------------------------------------------")

while number !=(0, 1, 2, 3, 4, 5):
    # creating and setting ticket number
    ticket_number = 2000
    # invoking function to print options
    menu_options()
    # user input to select menu item
    number = int(input("Enter menu selection 0-5 : "))
    if number == 0:
        print("The program has been terminated, goodbye.")
        quit()
    while number == 1:
        ticket_number += 1
        staff_id = input(str("Enter your staff ID: "))
        staff_name = input("Enter your name: ")
        staff_email = input("Enter your email address: ")
        print("If you require a new password type: Password change ")
        ticket_issue = input("Enter the description of the problem: ")
        if ticket_issue=="Password change" or ticket_issue=="password change":
            staff_id_list = list(staff_id)
            staff_name_list = list(staff_name)
            a = ''.join(staff_id_list[:2])
            b = ''.join(staff_name_list[:3])
            response = print("Response: Your new password is ",(a+b))
            ticket_status = "closed"
            next_issue = str(input("Do you have another issue to submit? (Y/N) \n"))
            if next_issue in("y","Y","YES","yes","Yes"):
                number = 1
            else:
                number = ()
        else:
            response = print("Response: Not yet provided.")
            ticket_status = "open"
            next_issue = str(input("Do you have another issue to submit? (Y/N) \n"))
            if next_issue in("y","Y","YES","yes","Yes"):
                number = 1
            else:
                number = ()


# creating a function with a parameter for ticket details
# I need to split these into smaller functions
def show_ticket_details(ticket_number, staff_id, staff_name, staff_email, ticket_issue, ticket_status):
    print("Ticket: {0} \n"
          "Submitted by Staff ID: {1}\n"
          "Ticket Owner: {2}\n"
          "Contact email address: {3}\n"
          "Description of issue: {4}\n"
          "Ticket status: {5}\n"
          .format(ticket_number, staff_id, staff_name, staff_email, ticket_issue, ticket_status))
    return ticket_number
    
# invoking the function, will print the ticket details
show_ticket_details(ticket_number, staff_id, staff_name, staff_email, ticket_issue, ticket_status)
    
  
    

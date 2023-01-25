# TestHelpdeskTicketSystem4.py
#
# Author: K.A Warmington
# Date: 16 January 2023

print("IT5016D Helpdesk Ticket System")

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

ticket_list = []

class Ticket:
    "A ticket class"
        
    def __init__(self, id, staff_id, name, email, issue, status, response):

        # class ticket, ticket number is the ID
        self.id = id
        self.staff_id = staff_id
        self.name = name
        self.email = email
        self.issue = issue
        self.status = status
        self.response = response

    def __str__(self):
        return ("Ticket #: {self.id}\nSubmitted by staff ID:"
    "{self.staff_id}\nTicket owner: {self.name}\nContact email address:"
    "{self.email}\nDescription of issue:{self.issue}\nIssue response:"
    "{self.response}\nTicket status: {self.status}")

    def create_ticket(id, staff_id, name, email, issue, response, status):
        id = len(ticket_list) + 2001
        staff_id = str(input("Enter your staff ID: "))
        name = input("Enter your name: ")
        email = input("Enter your email address: ")
        issue = input("If you require a new password type:Password change\n"
                      "Enter the description of the problem: ")
        if issue=="Password change" or issue=="password change":
            staff_id_list = list(staff_id)
            name_list = list(name)
            a = ''.join(staff_id_list[:2])
            b = ''.join(name_list[:3])
            response = ("Response: Your new password is ",(a+b))
            status = "closed"
        else:
            response = "Response: Not yet provided."
            status = "open"
        new_ticket = Ticket(id, staff_id, name, email, issue, status, response)
        ticket_list.append(new_ticket)
        print("Thank you, your ticket has been logged. Ticket #:", id)

    def view_tickets(ticket):
        return ()

    def update_response(ticket_id):
        for ticket in ticket_list:
            if ticket.id == ticket_id:
                response = input("Please enter the new response:")
                ticket.reponse = response
                print("Response updated successfully")
                return
            print("Ticket #: {ticket_id} not found.")

    def update_status(ticket_id):
        for ticket in ticket_list:
            if ticket.id == ticket_id:
                status = input("Please enter the new status:")
                ticket.status = status
                print("Status updated successfully")
                return
            print("Ticket #: {ticket_id} not found.")

    def ticket_stats(ticket_id):
        number_of_tickets = ticket_list.count(ticket_id)
        print("Number of tickets created:", number_of_tickets)
        number_of_resolved = ticket_list.count("closed" + "Closed")
        print("Number of resolved tickets:", number_of_resolved)
        number_of_open = ticket_list.count("open" + "Open")
        print("Number of Open tickets:", number_of_open)
                

while True:
    menu_options()
    action = int(input("Enter menu selection 0-5 : "))
    if action == 0:
        print("The program has been terminated, goodbye.")
        break
    elif action == 1:
        create_ticket()
    elif action == 2:
        view_ticket()
    elif action == 3:
        ticket_id = int(input("Please enter the ID of the ticket: "))
        update_response(ticket_id)
    elif action == 4:
        ticket_id = int(input("Please enter the ID of the ticket: "))
        update_status(ticket_id)
    elif action == 5:
        ticket_stats()
    else:
        print("Invalid entry. Please try again.")
        
        
    
    
        
    

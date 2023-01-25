# HelpdeskTicketSystem3.py
#
# Author: K.A Warmington
# Date: 16 January 2023
from abc import ABC

print("IT5016D Helpdesk Ticket System")


def menu_options():
    print("------------------------------------------------------------\n"
          "Select from the following choices.\n"
          "0: Exit and end the program \n"
          "1: Submit helpdesk ticket \n"
          "2: Show all tickets \n"
          "3: Respond to ticket by number \n"
          "4: Reopen a closed ticket \n"
          "5: Display ticket stats \n"
          "------------------------------------------------------------")

tickets = []


class Ticket(ABC):
    def __init__(self, number, staff_id, name, email, issue, status, response):
        # class ticket, ticket number is the ID
        self.number = number
        self.staff_id = staff_id
        self.name = name
        self.email = email
        self.issue = issue
        self.status = status
        self.response = response
    """A ticket class"""

    def __str__(self):
        return  ('Ticket #: {self.number}\nSubmitted by staff ID:'
                '{self.staff_id}\nTicket owner: {self.name}\nContact email address:'
                '{self.email}\nDescription of issue:{self.issue}\nIssue response:'
                '{self.response}\nTicket status: {self.status}')

def create_ticket():
    number = len(tickets) + 2001
    staff_id = str(input("Enter your staff ID: "))
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    issue = input("If you require a new password type:Password change\n"
                  "Enter the description of the problem: ")
    if issue == "Password change" or issue == "password change":
        staff_id_list = list(staff_id)
        name_list = list(name)
        a = ''.join(staff_id_list[:2])
        b = ''.join(name_list[:3])
        response = print("Response: Your new password is", (a + b))
        status = "closed"
    else:
        response = "Response: Not yet provided."
        print(response)
        status = "open"
    new_ticket = {"ticket number": number,
                  "staff id": staff_id,
                  "staff name": name,
                  "staff email": email,
                  "issue": issue,
                  "status": status,
                  "response": response}
    tickets.append(new_ticket)
    print("Thank you, your ticket has been logged. Ticket #:", number)

def view_tickets():
    print (new_ticket)

def update_response():
    for Ticket in tickets:
        if Ticket.number == Ticket.number:
            response = input("Please enter the new response:")
            Ticket.reponse = response
            print("Response updated successfully")
            return
        print("Ticket #: {ticket_number} not found.")

def update_status():
    for Ticket in tickets:
        if Ticket.new_ticket == Ticket.number:
            status = input("Please enter the new status:")
            Ticket.status = status
            print("Status updated successfully")
            return
        print("Ticket #: {ticket_id} not found.")

def ticket_stats():
    number_of_tickets = tickets.count(ticket_id)
    print("Number of tickets created:", number_of_tickets)
    number_of_resolved = tickets.count("closed" + "Closed")
    print("Number of resolved tickets:", number_of_resolved)
    number_of_open = tickets.count("open" + "Open")
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
        view_tickets()
    elif action == 3:
        ticket_id = int(input("Please enter the ID of the ticket: "))
        update_response()
    elif action == 4:
        ticket_id = int(input("Please enter the ID of the ticket: "))
        update_status()
    elif action == 5:
        ticket_stats()
    else:
        print("Invalid entry. Please try again.")

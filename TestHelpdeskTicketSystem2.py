# TestHelpdeskTicketSystem2.py
#
# @Author K W Warmington
# Date 03.01.2023

ticket_list = []

class Ticket:
    def __init__(self, id, subject, description, priority):
        self.id = id
        self.subject = subject
        self.description = description
        self.priority = priority
        self.status = "Open"
    
    def __str__(self):
        return f'ID: {self.id}\nSubject: {self.subject}\nDescription: {self.description}\nPriority: {self.priority}\nStatus: {self.status}'

def create_ticket():
    id = len(ticket_list) + 1
    subject = input("Please enter the subject of the issue: ")
    description = input("Please enter a brief description of the issue: ")
    priority = input("Please enter the priority of the issue (Low, Medium, High): ")
    new_ticket = Ticket(id, subject, description, priority)
    ticket_list.append(new_ticket)
    print("Ticket created successfully!")

def view_ticket(ticket_id):
    for ticket in ticket_list:
        if ticket.id == ticket_id:
            print(ticket)
            return
    print(f"Ticket with ID {ticket_id} not found.")

def update_ticket(ticket_id):
    for ticket in ticket_list:
        if ticket.id == ticket_id:
            subject = input("Please enter the new subject of the issue: ")
            description = input("Please enter the new description of the issue: ")
            priority = input("Please enter the new priority of the issue (Low, Medium, High): ")
            ticket.subject = subject
            ticket.description = description
            ticket.priority = priority
            print("Ticket updated successfully!")
            return
    print(f"Ticket with ID {ticket_id} not found.")

def resolve_ticket(ticket_id):
    for ticket in ticket_list:
        if ticket.id == ticket_id:
            ticket.status = "Resolved"
            print("Ticket resolved successfully!")
            return
    print(f"Ticket with ID {ticket_id} not found.")

while True:
    action = input("What would you like to do? (Create, View, Update, Resolve, Exit) ")
    if action.lower() == "create":
        create_ticket()
    elif action.lower() == "view":
        ticket_id = int(input("Please enter the ID of the ticket: "))
        view_ticket(ticket_id)
    elif action.lower() == "update":
        ticket_id = int(input("Please enter the ID of the ticket: "))
        update_ticket(ticket_id)
    elif action.lower() == "resolve":
        ticket_id = int(input("Please enter the ID of the ticket: "))
        resolve_ticket(ticket_id)
    elif action.lower() == "exit":
        break
    else:
        print("Invalid action. Please try again.")

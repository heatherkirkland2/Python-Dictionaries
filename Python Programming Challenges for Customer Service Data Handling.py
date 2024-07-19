'''
Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement: Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.
Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
'''
class TicketTracker:
    def __init__(self):
        # Initialize with some sample tickets
        self.service_tickets = {
            "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
            "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
        }

    def open_ticket(self, customer, issue):
        """Open a new service ticket."""
        ticket_id = f"Ticket{len(self.service_tickets) + 1:03d}"
        self.service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"New ticket {ticket_id} opened for {customer}.")

    def update_status(self, ticket_id, status):
        """Update the status of an existing ticket."""
        if ticket_id in self.service_tickets:
            self.service_tickets[ticket_id]["Status"] = status
            print(f"Ticket {ticket_id} status updated to {status}.")
        else:
            print(f"Ticket {ticket_id} not found.")

    def display_tickets(self, status=None):
        """Display all tickets or filter by status."""
        for ticket_id, details in self.service_tickets.items():
            if status is None or details["Status"] == status:
                print(f"{ticket_id}: Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")

# Example usage
tracker = TicketTracker()
tracker.open_ticket("Charlie", "Connectivity issue")
tracker.update_status("Ticket001", "closed")
tracker.display_tickets()
tracker.display_tickets("open")

#  Hint:  You may not need all of these.  Remove the unused functions.

'''
Plan:
    The first item in the array will have a source of None. 
    The following ticket will have a source that matches the destination of the ticket before it
    When you find the order of the ticket, place the destination in the array, the last item in the array will be None

    Store the data in a dictionary {source: destination}
'''

'PASSES ALL TESTS'

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Store the data in a dictionary {source: destination}
    d = {}

    for i in range(length):
        d[tickets[i].source] = tickets[i].destination

    # Populate a return array with slots for number of tickets
    arr = [0] * length

    # The first item is always the ticket with None as the source (key)
    arr[0] = d['NONE']

    # Look for the next ticket
    # For i location, use i-1's destination (value) as the key to search for
    # Add that key's value to the final array
    # Skip the first i location
    for i in range(1, length):
        key = arr[i-1]
        arr[i] = d[key]
    
    # Return the array
    return arr



# Run example

# class Ticket:
#     def __init__(self, source, destination):
#         self.source = source
#         self.destination = destination

# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]


# print(reconstruct_trip(tickets, len(tickets)))

#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    available_ticket = None

    for i in range(length):
        departure = tickets[i].source
        arrival = tickets[i].destination

        hash_table_insert(hashtable, departure, arrival)

        # check if the ticket for your first flight has a destination with a source of NONE
        if departure == "NONE":
            available_ticket = arrival
            # set as starting location
            route[0] = available_ticket
    
    for i in range(1, length):
        next_destination = hash_table_retrieve(hashtable, available_ticket)
        route[i] = next_destination

        available_ticket = next_destination

    return route

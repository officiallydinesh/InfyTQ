def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    rate_per_adults=no_of_adults*37550.0 
    rate_per_children=no_of_children*(37550.0/3)
    servicetax=(no_of_children+no_of_adults)*2628.5
    total_ticket_cost=rate_per_children+rate_per_adults+servicetax
    discount=total_ticket_cost*0.10
    total_ticket_cost=total_ticket_cost-discount

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)

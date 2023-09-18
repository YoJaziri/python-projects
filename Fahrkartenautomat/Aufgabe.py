import json 

with open ("tickets.json", "r") as file:
    automat = json.load(file)
    
    
    
    tickets = automat["tickets"]
    # print (tickets)
    # print(type(tickets))
    possible_tickets = len(tickets)
    check = range(1, possible_tickets+1)
    # print (type(check))
    
    print (f'Hello Sir, there is {possible_tickets} possible tickets that you can purchase:\n')
    
    for i, x in enumerate(tickets, 1):
        print (f'{i}. {x["name"]}: {x["price"]} euro.')
        
    purchased_ticket = input(f'\nPlease enter the index of the ticket between 1 and {possible_tickets} that you want to purchase:\n')
    
    if purchased_ticket.isdigit() == True:
        purchased_ticket = int(purchased_ticket)
    else:
        print ("Invalid choice")
        exit()
    
    if purchased_ticket not in check:
        print ("Invalid choice")
        exit()
        
    dict_purchased_ticket = tickets[purchased_ticket-1]
    
    # print (type(dict_purchased_ticket))
        
    print (f'\nThe required ticket ({dict_purchased_ticket["name"]}) cost {dict_purchased_ticket["price"]} euro.\nThe machine accepts the following notes/coins:\n')
    accepted_cash = list (automat["accepted_cash"])
    for x in accepted_cash:
        print (f'{x} euro')
        
    price_to_pay = dict_purchased_ticket["price"]
    
    while price_to_pay > 0:
        payed = int(input(f'\nYou need to pay {price_to_pay} euro:\n'))
        if payed in accepted_cash:
            price_to_pay = price_to_pay - payed
        
        if price_to_pay == 0:
            print(f'Thank you, your ticket is printed')
        elif price_to_pay < 0:
            print(f'\nThank you, your ticket is printed and you receive {abs(price_to_pay)} euro back')
            
        
        
    
    
    
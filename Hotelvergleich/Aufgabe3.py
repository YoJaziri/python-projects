marrios = {
    "name" : "Marrios",
    "age" : 1999,
    "payment_options" : ["card","cash","online"],
    "available_rooms" : [800, 801, 802, 805, 900, 1000, 1001],
    "price_per_night" : 50,
    "employees" : ["carlo","maria","luis","fernando"]
}

hilten = {
    "name" : "Hilten",
    "age" : 1992,
    "payment_options" : ["card","online"],
    "available_rooms" : [100, 800, 801, 805, 1000, 1001],
    "price_per_night" : 70,
    "employees" : ["artur","maria","oliver","xenia"]
    
}

dauer = int(input("Wie lang möchten Sie übernachten? "))
cost_marrios = dauer * marrios["price_per_night"]
cost_hilten = dauer * hilten["price_per_night"]

prince_unterschied = abs(cost_hilten-cost_marrios)


print (f'{dauer} Übernachtungen kosten {cost_marrios}€ im Hotel Marrios und {cost_hilten}€ im Hotel Hilten. Der Preisunterschied sind {prince_unterschied}€')


zahlungs_marrios = len(marrios["payment_options"])
zahlungs_hilten = len(hilten["payment_options"])

print(f'Im Hotel Marrios gibt es {zahlungs_marrios} und im Hotel Hilten gibt es {zahlungs_hilten} Zahlungsmöglichkeiten')

diff = []
for elem in marrios["payment_options"]:
    if elem not in hilten["payment_options"]:
        diff.append(elem)


for elem2 in hilten["payment_options"]:
    if elem2 not in marrios["payment_options"]:
        diff.append(elem2)

print(f'die Hotels unterscheiden sich in den folgenden Zahlungsmöglichkeit {diff}')


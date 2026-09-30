fuel_type = input("What type of fuel do you want to use? ")
amount_fuel = 0.0
fuel_cost = 0.0

if fuel_type.lower() == "regular":
    amount_fuel = float(input("How many litres of fuel do you need? "))
    if(amount_fuel> 0):
        fuel_cost = amount_fuel * 1.42
        print(f"Cost: ${fuel_cost:.2f}")
    else:
        amount_fuel = float(input("How many litres of fuel do you need? "))
elif fuel_type.lower() == "extra":
    amount_fuel = float(input("How many litres of fuel do you need? "))
    if (amount_fuel > 0):
        fuel_cost = amount_fuel * 1.53
        print(f"Cost: ${fuel_cost:.2f}")
    else:
        amount_fuel = float(input("How many litres of fuel do you need? "))
elif fuel_type.lower() == "premium":
    amount_fuel = float(input("How many litres of fuel do you need? "))
    if (amount_fuel > 0):
        fuel_cost = amount_fuel * 1.60
        print(f"Cost: ${fuel_cost:.2f}")
    else:
        amount_fuel = float(input("How many litres of fuel do you need? "))
elif fuel_type.lower() == "diesel":
    amount_fuel = float(input("How many litres of fuel do you need? "))
    if (amount_fuel > 0):
        fuel_cost = amount_fuel * 1.75
        print(f"Cost: ${fuel_cost:.2f}")
    else:
        amount_fuel = float(input("How many litres of fuel do you need? "))
else:
    print("Invalid fuel type")

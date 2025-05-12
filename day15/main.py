#Coffee_Machine 
resource=input("What would you like to order? (espresso, latte, cappuccino): ")

if resource=="report":
    print("Water: 300ml")
    print("Milk: 200ml")
    print("Coffee: 100g")
    print("Money: $2.5")



if resource=="espresso":
    print("Please insert coins.")
    inserted_coins = int(input("How many quarters? ")) * 0.25
    inserted_coins += int(input("How many dimes? ")) * 0.10
    inserted_coins += int(input("How many nickles? ")) * 0.05
    inserted_coins += int(input("How many pennies? ")) * 0.01
    print(f"Inserted coins: ${inserted_coins:.2f}")
    if inserted_coins >= 1.50:
        change = inserted_coins - 1.50
        print(f"Here is your change: ${change:.2f}")
        print("Here is your espresso. Enjoy!")
    else:
        print("Sorry, that's not enough money. Money refunded.")    
if resource=="latte":
    print("Please insert coins.")
    inserted_coins = int(input("How many quarters? ")) * 0.25
    inserted_coins += int(input("How many dimes? ")) * 0.10
    inserted_coins += int(input("How many nickles? ")) * 0.05
    inserted_coins += int(input("How many pennies? ")) * 0.01
    print(f"Inserted coins: ${inserted_coins:.2f}")
    if inserted_coins >= 2.50:
        change = inserted_coins - 2.50
        print(f"Here is your change: ${change:.2f}")
        print("Here is your latte. Enjoy!")
    else:
        print("Sorry, that's not enough money. Money refunded.")
if resource=="cappuccino":
    print("Please insert coins.")
    inserted_coins = int(input("How many quarters? ")) * 0.25
    inserted_coins += int(input("How many dimes? ")) * 0.10
    inserted_coins += int(input("How many nickles? ")) * 0.05
    inserted_coins += int(input("How many pennies? ")) * 0.01
    print(f"Inserted coins: ${inserted_coins:.2f}")
    if inserted_coins >= 3.00:
        change = inserted_coins - 3.00
        print(f"Here is your change: ${change:.2f}")
        print("Here is your cappuccino. Enjoy!")
    else:
        print("Sorry, that's not enough money. Money refunded.")
        

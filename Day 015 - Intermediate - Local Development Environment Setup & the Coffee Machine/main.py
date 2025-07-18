from menu import *

def report():
    return (f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}")

def is_resource_sufficient(ingredients):
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            return False, ingredient
    return True, None

def process_order(ingredients, cost):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    resources["money"] += cost

def read_coins():
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return pennies * 0.01 + nickels * 0.05 + dimes * 0.10 + quarters * 0.25

while True:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    
    if prompt == "off":
        print("Turning off the coffee machine...")
        break
        
    elif prompt == "report":
        print(report())

    elif prompt in drinks:
        drink = prompt
        ingredients = MENU[drink]["ingredients"]
        cost = MENU[drink]["cost"]

        sufficient, missing_ingredient = is_resource_sufficient(ingredients)
        if sufficient:
            money = read_coins()
            if money >= MENU[drink]["cost"]:
                if money > cost:
                    change = money - cost
                    money -= change
                    print(f"Here is ${change:.2f} in change.")
                process_order(ingredients, money)
                print(f"Here is your {drink} ☕. Enjoi!")
            else:
                print("Sorry, you don't have enough money. Money refunded.")
        else:
            print(f"Not enough {missing_ingredient}!")

    else:
        print("Enter a valid option (espresso/latte/cappuccino/report/off)).")
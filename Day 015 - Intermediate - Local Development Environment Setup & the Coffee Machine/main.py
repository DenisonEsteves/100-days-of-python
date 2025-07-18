from menu import *

def report():
    return (f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}")

def check_resourses(type_coffee):
    if resources["water"] < MENU[type_coffee]["ingredients"]["water"]: return "water"
    if resources["milk"] < MENU[type_coffee]["ingredients"]["milk"]: return "milk"
    if resources["coffee"] < MENU[type_coffee]["ingredients"]["coffee"]: return "coffee"
    else: return "enough"

def process_order(type_coffee):
    resources["water"] -= MENU[type_coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[type_coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[type_coffee]["ingredients"]["coffee"]
    resources["money"] += MENU[type_coffee]["cost"]

while True:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")

    if prompt == "off":
        print("Turning off the coffee machine.")
        break

    if prompt == "report":
        print(report())

    elif prompt in types_coffee:
        type_coffee = prompt
        resource = check_resourses(type_coffee)
        if resource == "enough":
            print("Please insert coins.")

            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            money = pennies * 0.01 + nickels * 0.05 + dimes * 0.10 + quarters * 0.25

            if money >= MENU[type_coffee]["cost"]:
                if money > MENU[type_coffee]["cost"]:
                    change = money - MENU[type_coffee]["cost"]
                    money -= change
                    print(f"Here is ${change:.2f} in change.")
                process_order(type_coffee)
                print(f"Here is your {type_coffee} ☕. Enjoi!")
            else: print("Sorry, you don't have enough money. Money refunded.")

        else: print(f"Sorry, there is not enough {resource}.")

    else: print("Enter a valid option.")








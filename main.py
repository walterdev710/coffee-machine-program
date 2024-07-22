from data import MENU, resources


money = 0

def is_sufficient(order_ingredients):
    """It checks whether resource is enough or not. If resource is enough it returns True. Otherwise false"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry we don't have enough {item}.")
            return False
    return True 

def process_coin():
    """Returns the total calculated from coins inserted"""
    print("Please, Insert coin!")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when money is enough for drink. Return false when money is not enough"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here's your {change} in change")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry, that's not enough  money. Money refunded.")
        return False

def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}")

# Input for asking what kind of coffee user needs
is_on = True
while is_on:
    usr = input("What would you like? (espresso/latte/cappuccino): ")
    if usr == "off":
        is_on = False
    elif usr == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[usr]
        if is_sufficient(drink["ingredients"]): 
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(usr, drink["ingredients"])



from art import logo
import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 18,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 23,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 37,
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
}


def take_coins(cost):
    print("Please insert coins.")
    paid = False
    while not paid:
        coins1rs = int(input("How many 1 rupee coins? "))
        coins2rs = int(input("How many 2 rupee coins? "))
        coins5rs = int(input("How many 5 rupee coins? "))
        coins10rs = int(input("How many 10 rupee coins? "))
        total = coins1rs + 2 * coins2rs + 5 * coins5rs + 10 * coins10rs
        if total > cost:
            change = total - cost
            print(f"Here's your change {change}Rs. Enjoy your coffee!")
            paid = True
        elif total == cost:
            print("Its exact change!! Enjoy your coffee!")
            paid = True
        else:
            amt_less = cost - total
            print(f"The cost of your coffee is {cost} and you paid {total}. "
                  f"Please pay the balance amount {amt_less}")
            cost = cost - total


def stock_update(stock, ingredient):
    for i in ingredient:
        stock[i] -= ingredient[i]


def print_resources(stock):
    print("Stock Check: \n")
    for i in stock:
        print(f"{i}: {stock[i]}")


def check_availability(stock, ingredients):
    for i in ingredients:
        if ingredients[i] > stock[i]:
            return False
    return True


print(logo)
print("Hello!!!")
should_continue = True
while should_continue:
    order = int(input("What would you like to have?? Press 1. for Espresso \n2. for Latte "
                      "3. for Cappuccino 4. Report available\n"))

    if order == 1:
        order = MENU["espresso"]
        if check_availability(resources, order["ingredients"]):
            print(f'That would be {order["cost"]}Rs.')
            take_coins(order["cost"])
            stock_update(resources, order["ingredients"])
            print("There you go, your espresso.Enjoy!")
            os.system('clear')
            print(logo)
        else:
            print("Sorry we are out of ingredients.")
            should_continue = False

    elif order == 2:
        order = MENU["latte"]
        if check_availability(resources, order["ingredients"]):
            print(f'That would be {order["cost"]}Rs.')
            take_coins(order["cost"])
            stock_update(resources, order["ingredients"])
            print("There you go, your latte.Enjoy!")
            os.system('clear')
            print(logo)
        else:
            print("Sorry we are out of ingredients.")
            should_continue = False
    elif order == 3:
        order = MENU["cappuccino"]
        if check_availability(resources, order["ingredients"]):
            print(f'That would be {order["cost"]}Rs.')
            take_coins(order["cost"])
            stock_update(resources, order["ingredients"])
            print("There you go, your cappuccino.Enjoy!")
            os.system('clear')
            print(logo)
        else:
            print("Sorry we are out of ingredients.")
            should_continue = False
    elif order == 4:
        print_resources(stock=resources)
        os.system("clear")
        print(logo)


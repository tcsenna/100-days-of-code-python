MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def nao_tem(choice, resources):
    ingr = MENU[choice]['ingredients']
    faltou = []
    for i in ingr:
        if resources[i] < ingr[i]:
            faltou.append(i)
            break
    return faltou


def process_order(choice, accum):
    price = MENU[choice]["cost"]
    q = int(input("How many quarters? \n"))
    d = int(input("How many dimes? \n"))
    n = int(input("How many nickles? \n"))
    p = int(input("How many pennies? \n"))
    paid = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    if paid < price:
        print("Sorry that's not enough money. Money refunded.")
        return (False, accum)
    elif paid > price:
        change = round(paid - price, 2)
        print(f"Here is ${change} in change.\nHere is your {choice} ☕️. Enjoy!")
        accum += price
        return (True, accum)
    else:
        print(f"Here is your {choice} ☕️. Enjoy!")
        accum += price
        return (True, accum)


def update_resource(res, choice):
    ingred = MENU[choice]['ingredients']
    for i in ingred:
        res[i] -= ingred[i]
    return res


def print_report(accum, res):
    print(f"Water: {res['water']}\nMilk: {res['milk']}\nCoffee: {res['coffee']}\nMoney: {accum}")


def coffee_machine(res, accum=0):
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        exit()
    elif choice == 'report':
        print_report(accum, res)
    else:
        need = nao_tem(choice, res)
        if len(need) > 0: #ou seja, faltou algum ingrediente
            print(f"Sorry there is not enough {need[0]}.")
        else:
            print("Please insert coins.")
            paid, accum = process_order(choice, accum)
            if paid:
                res = update_resource(res, choice)

    coffee_machine(res, accum)

coffee_machine(resources)

from data import MENU, resources

# available resources
water = resources["water"]
milk = resources["milk"]
coffees = resources["coffee"]
money = 0
on = True

while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        on = False

    if choice == "report":
        print(f"Water left: {water}\n Milk left: {milk}\n Coffee left: {coffees}\n money gained: {money}")

    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        cost_of_coffee = MENU[choice]["cost"]
        required_water = MENU[choice]["ingredients"]["water"]
        required_milk = MENU[choice]["ingredients"]["milk"]
        required_coffee = MENU[choice]["ingredients"]["coffee"]

        if water >= required_water and milk >= required_milk and coffees >= required_coffee:
            quarters = int(input("quarters: "))
            dimes = int(input("dimes: "))
            nickels = int(input("nickel: "))
            pennies = int(input("pennies: "))
            given_money = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
            water -= required_water
            milk -= required_milk
            coffees -= required_coffee
            if given_money >= cost_of_coffee:
                money += cost_of_coffee
                print(f"Here's your {choice}")
                print(f"Water left: {water}\n Milk left: {milk}\n Coffee left: {coffees} ")
                print(f"Your change: {given_money - cost_of_coffee}")
            else:
                print("not enough money, lol.... That's what she said BTW your moneys refunded")

        else:
            print("you are out of resources, Try something different")
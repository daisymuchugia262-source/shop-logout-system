
from display_products import display_products
from adding_item import choosing_items, basket
from removing_item import remove_items
from calculating_total import calculate_total
from payment import payment
from receipt import print_receipt


def main():
    print("WELCOME TO SMART SHOP")

    display_products()

    choosing_items()

    while True:
        answer = input("Do you want to remove an item? (yes/no): ").lower()

        if answer == "yes":
            remove_items()
        elif answer == "no":
            break
        else:
            print("Please enter yes or no.")

    if not basket:
        print("Your basket is empty. No purchase made.")
        return

    subtotal, discount, total = calculate_total()

    change = payment(total)

    print_receipt(subtotal, discount, total, change)


main()
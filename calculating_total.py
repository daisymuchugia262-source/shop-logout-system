
from display_products import products
from adding_item import basket


def calculate_total():
    subtotal = 0

    for serial, quantity in basket.items():
        price = products[serial]["price"]
        line_total = price * quantity

        print(products[serial]["name"])
        print("Quantity:", quantity)
        print("Line total: KSh", line_total)

        subtotal = subtotal + line_total

    if subtotal >= 2000:
        discount = subtotal * 10 / 100
    elif subtotal >= 1000:
        discount = subtotal * 5 / 100
    else:
        discount = 0

    total = subtotal - discount

    print("Subtotal: KSh", subtotal)
    print("Discount: KSh", discount)
    print("Final total: KSh", total)

    return subtotal, discount, total
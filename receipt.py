
from display_products import products
from adding_item import basket


def print_receipt(subtotal, discount, total, change):
    print("\n======= SMART SHOP RECEIPT =======")

    for serial, quantity in basket.items():
        print("Item:", products[serial]["name"])
        print("Quantity:", quantity)
        print("Price: KSh", products[serial]["price"])
        print("Line total: KSh",
              products[serial]["price"] * quantity)

    print("Subtotal: KSh", subtotal)
    print("Discount: KSh", discount)
    print("Total: KSh", total)
    print("Change: KSh", change)
    print("Thank you for shopping")
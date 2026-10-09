from display_products import products
from adding_item import basket

def remove_items():
    if not basket:
        print("Your basket is empty")
        return
    for serial,quantity in basket.items():
        print(products[serial]["name"],"Quantity:", quantity)

    choose=input("Enter product you want to remove").upper()

    if choose in basket:
        del basket[choose]
        print("Item removed successfully.")
    else:
        print("Item not found in basket")

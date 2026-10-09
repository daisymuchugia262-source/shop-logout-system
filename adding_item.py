from display_products import products
basket= {}   
def choosing_items():
    while True:
        choose = input("What is the serial number of the product you want?").upper()

        if choose == "DONE":
            break
        if choose not in products:
            print("Invalid serial number")
            continue
    
        quantity=int(input("How many do you want?"))

        if choose in basket:
            basket[choose]+=quantity
        else:
            basket[choose]=quantity

        print("Item:", products[choose]["name"])
        print("Quantity added:", quantity)
        print("Item added sucessfully")
    return basket
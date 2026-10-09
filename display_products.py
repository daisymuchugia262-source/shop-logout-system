products = {
    "juzsvw": {"name": "Laptop", "price": 40000},
    "UVRHRE": {"name": "JSJZ speaker", "price": 15000},
    "WRHGDUI": {"name": "JBL speaker", "price": 20000},
    "DJJDGEKD": {"name": "Orimo bluetooth", "price": 4000},
    "AUGDYUIE": {"name": "Orimo headphones", "price": 7000},
}

def display_products():
    for serial, product in products.items():
        print("Serial Number:", serial)
        print("Item:", product["name"])
        print("Price:", product["price"])
        print()
# Smart Shop Checkout System

A simple command-line checkout program written in Python. It displays a small product catalog, lets a customer build and edit a basket, applies a discount, accepts payment, and prints a receipt. Prices are shown in Kenyan shillings (KSh).

## Features

- Displays products with serial numbers and prices.
- Adds products and quantities to a shopping basket.
- Removes a selected product from the basket.
- Calculates subtotal and applies a discount:
  - 5% for subtotals from KSh 1,000 up to (but not including) KSh 2,000.
  - 10% for subtotals of KSh 2,000 or more.
- Rejects payments below the final total and calculates change.
- Prints an itemized receipt.

## Requirements

- Python 3
- No external packages are required.

## Run the program

Open a terminal in the `shop checkout system` folder and run:

```bash
python main.py
```

On some systems, use `python3 main.py` instead.

## How to use it

1. Review the products and their serial numbers.
2. Enter a product serial number and quantity when prompted. Enter `DONE` when you have finished adding items.
3. Choose whether to remove a product from the basket. Enter `yes` or `no`; if removing, enter its serial number.
4. Enter a payment amount at least equal to the final total.
5. Review the receipt and any change due.

Serial numbers are case-insensitive in the prompts. The current product list and prices are in `display_products.py`.

## Project files

| File | Purpose |
| --- | --- |
| `main.py` | Runs the checkout flow and connects the other modules. |
| `display_products.py` | Stores the product catalog and displays it. |
| `adding_item.py` | Collects products and quantities for the basket. |
| `removing_item.py` | Removes a product from the basket. |
| `calculating_total.py` | Calculates line totals, subtotal, discount, and final total. |
| `payment.py` | Collects payment and calculates change. |
| `receipt.py` | Prints the itemized receipt. |

## Notes

This is a small learning project. Basket and product data are kept in memory while the program runs and are not saved after it exits.

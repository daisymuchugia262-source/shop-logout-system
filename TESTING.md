# Testing

## Manual test checklist

Run the program from the `shop checkout system` folder:

```bash
python main.py
```

Use `python3 main.py` if your system uses that command.

| Check | Steps | Expected result |
| --- | --- | --- |
| Product display | Start the program. | The product serial numbers, names, and prices are displayed. |
| Add an item | Enter a listed serial number and a positive quantity, then enter `DONE`. | The item and quantity are added to the basket. |
| Invalid serial number | Enter a serial number that is not listed. | The program reports an invalid serial number and prompts again. |
| Remove an item | Add an item, answer `yes` to the removal prompt, then enter its serial number. | The item is removed from the basket. |
| Empty basket | Enter `DONE` without adding any items. | The program reports the basket is empty and ends without taking payment. |
| 5% discount | Add items totaling KSh 1,000–1,999. | A 5% discount is applied. |
| 10% discount | Add items totaling KSh 2,000 or more. | A 10% discount is applied. |
| No discount | Add items totaling less than KSh 1,000. | No discount is applied. |
| Insufficient payment | Enter an amount below the final total. | The program rejects it and asks for payment again. |
| Successful payment | Enter an amount equal to or above the final total. | Payment succeeds and change is calculated. |
| Receipt | Complete a purchase. | The receipt lists purchased items, quantities, prices, subtotal, discount, total, and change. |

## Current limitations

- These are manual checks; the project does not currently include automated tests.
- Enter a valid whole-number quantity and a numeric payment amount.
- Basket contents are not saved after the program exits.

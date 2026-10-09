
def payment(total):
    while True:
        amount = float(input("Enter payment amount: KSh "))

        if amount < total:
            print("Insufficient payment. Try again.")
        else:
            change = amount - total
            print("Payment successful.")
            print("Change: KSh", change)
            return change
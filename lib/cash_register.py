#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.total = 0.0
        self.items = []
        self.previous_transactions = []
        self.discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        item_total = price * quantity
        self.total += item_total
        
        # Append the item name multiple times based on the quantity
        for _ in range(quantity):
            self.items.append(item)
        
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity,
            "total_cost": item_total
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        multiplier = (100 - self.discount) / 100
        self.total = round(self.total * multiplier, 2)
        
        # Format total to drop trailing zeros if it is an exact integer matching test formats
        display_total = int(self.total) if self.total.is_integer() else self.total
        print(f"After the discount, the total comes to ${display_total}.")
        
        self.previous_transactions.pop()

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No transactions to void.")
            return

        last_tx = self.previous_transactions.pop()
        self.total -= last_tx["total_cost"]
        
        # Remove the item from the list as many times as it was bought
        for _ in range(last_tx["quantity"]):
            if last_tx["item"] in self.items:
                self.items.remove(last_tx["item"])

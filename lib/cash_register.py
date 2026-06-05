#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize attributes
        self._discount = 0  # Internal variable for property tracking
        self.total = 0.0
        self.items = []
        self.previous_transactions = []
        
        # Set discount using the setter method for validation
        self.discount = discount

    @property
    def discount(self):
        """Getter for discount."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """Setter for discount with validation rules."""
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        """Adds an item, updates the total, and logs the transaction."""
        item_total = price * quantity
        self.total += item_total
        self.items.append(item)
        
        # Store transaction details for potential voids/discounts
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity,
            "total_cost": item_total
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        """Applies the discount percentage to the total and updates logs."""
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        # Calculate discount multiplier 
        multiplier = (100 - self.discount) / 100
        self.total = round(self.total * multiplier, 2)
        
        # Remove the last transaction tracking record as required
        self.previous_transactions.pop()

    def void_last_transaction(self):
        """Reverses the last added item completely."""
        if not self.previous_transactions:
            print("No transactions to void.")
            return

        # Remove last transaction 
        last_tx = self.previous_transactions.pop()
        self.total -= last_tx["total_cost"]
        
        if last_tx["item"] in self.items:
            self.items.remove(last_tx["item"])

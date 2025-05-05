#!/usr/bin/env python3

"""
A simple command-line checkbook application.

Features:
- Deposit money
- Withdraw money (with insufficient funds check)
- Display current balance
- Input validation for numeric values and positive amounts
"""

class Checkbook:
    """A class to manage a simple checkbook balance."""

    def __init__(self):
        """Initialize the checkbook with a zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook if sufficient funds exist.

        Args:
            amount (float): The amount to withdraw. Must be positive and <= balance.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Display the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main loop for the checkbook application.
    Prompts the user for actions until 'exit' is entered.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Exiting checkbook. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

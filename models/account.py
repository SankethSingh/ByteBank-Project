from abc import ABC


class Account(ABC):

    def __init__(
            self,
            account_no: int,
            name: str,
            email: str,
            password: int,
            balance: float = 0.0
    ):

        self.account_no = account_no
        self.name = name
        self.email = email
        self.password = password
        self.balance = balance

    # -------------------------
    # Getters
    # -------------------------

    def get_account_number(self):

        return self.account_no

    def get_name(self):

        return self.name

    def get_email(self):

        return self.email

    def get_balance(self):

        return self.balance

    # -------------------------
    # Account Operations
    # -------------------------

    def deposit(self, amount):

        if amount <= 0:
            return "Deposit amount should be greater than 0."

        self.balance += amount

        return f"₹{amount} deposited successfully."

    def withdraw(self, amount):

        if amount <= 0:
            return "Withdrawal amount should be greater than 0."

        if amount > self.balance:
            return "Insufficient Balance."

        self.balance -= amount

        return f"₹{amount} withdrawn successfully."

    def check_balance(self):

        return f"Current Balance : ₹{self.balance}"

    # -------------------------
    # Display Account Details
    # -------------------------

    def account_details(self):

        return {
            "Account Number": self.account_no,
            "Name": self.name,
            "Email": self.email,
            "Balance": self.balance
        }
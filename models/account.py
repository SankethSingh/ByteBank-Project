from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(
            self,
            acc_no: str,
            name: str,
            email: str,
            phone: str,
            pin_hash: str,
            balance: float = 0.0,
            status: str = "active",
            created_date: str = None
    ):

        self.acc_no = acc_no
        self.name = name
        self.email = email
        self.phone = phone
        self.pin_hash = pin_hash
        self.balance = balance
        self.status = status
        self.created_date = created_date

    # -------------------------
    # Getters
    # -------------------------

    def get_account_number(self):
        return self.acc_no

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
        """Base implementation. Subclasses override this for
        minimum balance or overdraft rules."""

        if amount <= 0:
            return "Withdrawal amount should be greater than 0."

        if amount > self.balance:
            return "Insufficient Balance."

        self.balance -= amount

        return f"₹{amount} withdrawn successfully."

    def check_balance(self):
        return f"Current Balance : ₹{self.balance}"

    # -------------------------
    # Abstract method — every subclass MUST implement this
    # -------------------------

    @abstractmethod
    def get_account_type(self):
        pass

    # -------------------------
    # Display Account Details
    # -------------------------

    def account_details(self):
        return {
            "Account Number": self.acc_no,
            "Name": self.name,
            "Email": self.email,
            "Phone": self.phone,
            "Balance": self.balance,
            "Status": self.status,
            "Created Date": self.created_date
        }
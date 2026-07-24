"""
models/user.py

Represents a ByteBank customer profile, decoupled from individual accounts.
A single User can own multiple Account objects (savings and/or current).
"""

class User:
    def __init__(self, user_id, name, email, phone, pin_hash,
                 status="active", created_date=None):
        self.user_id = user_id          # unique customer ID, separate from acc_no
        self.name = name
        self.email = email
        self.phone = phone
        self.pin_hash = pin_hash
        self.status = status            # active / blocked
        self.created_date = created_date
        self.accounts = []              # list of Account objects owned by this user

    def add_account(self, account):
        """Links a new Account object to this user profile."""
        self.accounts.append(account)

    def get_account(self, acc_no):
        """Returns the Account object matching acc_no, or None."""
        for acc in self.accounts:
            if acc.acc_no == acc_no:
                return acc
        return None

    def total_balance(self):
        """Sums balances across all accounts owned by this user."""
        return sum(acc.balance for acc in self.accounts)

    def __repr__(self):
        return f"User({self.user_id}, {self.name}, accounts={len(self.accounts)})"
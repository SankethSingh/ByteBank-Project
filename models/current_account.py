from models.account import Account


class CurrentAccount(Account):

    OVERDRAFT_LIMIT = 5000

    def __init__(
            self,
            account_no: int,
            name: str,
            email: str,
            password: int,
            balance: float = 0.0
    ):

        super().__init__(
            account_no,
            name,
            email,
            password,
            balance
        )

        self.account_type = "Current"

    # -------------------------
    # Get Account Type
    # -------------------------

    def get_account_type(self):

        return self.account_type

    # -------------------------
    # Withdraw with Overdraft
    # -------------------------

    def withdraw(self, amount):

        if amount <= 0:

            return "Withdrawal amount should be greater than 0."

        if amount > self.balance + self.OVERDRAFT_LIMIT:

            return "Overdraft Limit Exceeded."

        self.balance -= amount

        return f"₹{amount} withdrawn successfully."

    # -------------------------
    # Get Overdraft Limit
    # -------------------------

    def get_overdraft_limit(self):

        return self.OVERDRAFT_LIMIT

    # -------------------------
    # Account Summary
    # -------------------------

    def account_summary(self):

        return {
            "Account Type": self.account_type,
            "Account Number": self.account_no,
            "Account Holder": self.name,
            "Balance": self.balance,
            "Overdraft Limit": self.OVERDRAFT_LIMIT
        }
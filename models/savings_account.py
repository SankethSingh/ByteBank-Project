from models.account import Account


class SavingsAccount(Account):

    INTEREST_RATE = 4.0

    MINIMUM_BALANCE = 1000

    def __init__(self, acc_no, name, email, phone, pin_hash,
                 balance=0.0, status="active", created_date=None,
                 interest_rate=4.0):

        super().__init__(acc_no, name, email, phone, pin_hash,
                          balance, status, created_date)

        self.account_type = "Savings"
        self.interest_rate = interest_rate


    # -------------------------
    # Get Account Type
    # -------------------------

    def get_account_type(self):

        return self.account_type

    # -------------------------
    # Calculate Interest
    # -------------------------

    def calculate_interest(self):

        interest = (self.balance * self.INTEREST_RATE) / 100

        return interest

    # -------------------------
    # Withdraw with Minimum Balance Check
    # -------------------------

    def withdraw(self, amount):

        if amount <= 0:

            return "Withdrawal amount should be greater than 0."

        if self.balance - amount < self.MINIMUM_BALANCE:

            return "Minimum balance should be maintained."

        self.balance -= amount

        return f"₹{amount} withdrawn successfully."

    # -------------------------
    # Account Summary
    # -------------------------

    def account_summary(self):

        return {
            "Account Type": self.account_type,
            "Account Number": self.acc_no,
            "Account Holder": self.name,
            "Balance": self.balance,
            "Interest Rate": f"{self.INTEREST_RATE}%"
        }
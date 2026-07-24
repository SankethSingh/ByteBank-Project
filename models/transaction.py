from models.account import Account


class Transaction:

    def deposit(self, account: Account, amount: float):

        if amount <= 0:
            return "Deposit amount should be greater than 0."

        account.balance += amount

        return f"""
Deposit Successful

Amount Deposited : ₹{amount}

Current Balance : ₹{account.balance}
"""


    def withdraw(self, account: Account, amount: float):

        return account.withdraw(amount)


    def transfer(self, sender: Account, receiver: Account, amount: float):

        if amount <= 0:
            return "Transfer amount should be greater than 0."

        if sender.balance < amount:
            return "Insufficient Balance."

        sender.balance -= amount

        receiver.balance += amount

        return f"""
Transfer Successful

Transferred Amount : ₹{amount}

Sender Balance : ₹{sender.balance}

Receiver Balance : ₹{receiver.balance}
"""


    def mini_statement(self, account: Account):

        return f"""
Mini Statement

Account Number : {account.account_no}

Account Holder : {account.name}

Account Type : {account.account_type}

Available Balance : ₹{account.balance}
"""
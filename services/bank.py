from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount
from models.transaction import Transaction


class Bank:

    def __init__(self):

        self.accounts = {}

        self.next_account_number = 1001

        self.transaction = Transaction()

    # ----------------------------------
    # Create Account
    # ----------------------------------

    def create_account(self, account_type, name, email, password, balance=0):

        account_no = self.next_account_number

        self.next_account_number += 1

        if account_type.lower() == "savings":

            account = SavingsAccount(
                account_no,
                name,
                email,
                password,
                balance
            )

        elif account_type.lower() == "current":

            account = CurrentAccount(
                account_no,
                name,
                email,
                password,
                balance
            )

        else:

            return "Invalid Account Type"

        self.accounts[account_no] = account

        return account

    # ----------------------------------
    # Find Account
    # ----------------------------------

    def find_account(self, account_no):

        return self.accounts.get(account_no)

    # ----------------------------------
    # Login
    # ----------------------------------

    def login(self, account_no, password):

        account = self.find_account(account_no)

        if account is None:

            return None

        if account.password == password:

            return account

        return None

    # ----------------------------------
    # Deposit
    # ----------------------------------

    def deposit(self, account_no, amount):

        account = self.find_account(account_no)

        if account is None:

            return "Account Not Found"

        return self.transaction.deposit(account, amount)

    # ----------------------------------
    # Withdraw
    # ----------------------------------

    def withdraw(self, account_no, amount):

        account = self.find_account(account_no)

        if account is None:

            return "Account Not Found"

        return self.transaction.withdraw(account, amount)

    # ----------------------------------
    # Transfer
    # ----------------------------------

    def transfer(self, sender_acc, receiver_acc, amount):

        sender = self.find_account(sender_acc)

        receiver = self.find_account(receiver_acc)

        if sender is None:

            return "Sender Account Not Found"

        if receiver is None:

            return "Receiver Account Not Found"

        return self.transaction.transfer(
            sender,
            receiver,
            amount
        )

    # ----------------------------------
    # Balance
    # ----------------------------------

    def check_balance(self, account_no):

        account = self.find_account(account_no)

        if account is None:

            return "Account Not Found"

        return account.check_balance()

    # ----------------------------------
    # Mini Statement
    # ----------------------------------

    def mini_statement(self, account_no):

        account = self.find_account(account_no)

        if account is None:

            return "Account Not Found"

        return self.transaction.mini_statement(account)

    # ----------------------------------
    # Display All Accounts
    # ----------------------------------

    def display_all_accounts(self):

        if not self.accounts:

            return "No Accounts Available"

        data = []

        for account in self.accounts.values():

            data.append(account.account_summary())

        return data
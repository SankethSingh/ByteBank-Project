from models.transaction import Transaction
from utils import file_handler


class Bank:

    def __init__(self, acc_store):
        self.acc_store = acc_store
        self.transaction = Transaction()

    def find_account(self, account_no):
        return self.acc_store.get(account_no)

    def deposit(self, account_no, amount):
        account = self.find_account(account_no)
        if account is None:
            return "Account Not Found"

        result = self.transaction.deposit(account, amount)
        file_handler.sync_account(account)
        file_handler.append_ledger(account.acc_no, "DEPOSIT", amount, account.balance)
        return result

    def withdraw(self, account_no, amount):
        account = self.find_account(account_no)
        if account is None:
            return "Account Not Found"

        result = self.transaction.withdraw(account, amount)
        file_handler.sync_account(account)
        file_handler.append_ledger(account.acc_no, "WITHDRAW", amount, account.balance)
        return result

    def transfer(self, sender_acc, receiver_acc, amount):
        sender = self.find_account(sender_acc)
        receiver = self.find_account(receiver_acc)

        if sender is None:
            return "Sender Account Not Found"
        if receiver is None:
            return "Receiver Account Not Found"

        result = self.transaction.transfer(sender, receiver, amount)
        file_handler.sync_account(sender)
        file_handler.sync_account(receiver)
        file_handler.append_ledger(sender.acc_no, "TRANSFER-OUT", amount, sender.balance)
        file_handler.append_ledger(receiver.acc_no, "TRANSFER-IN", amount, receiver.balance)
        return result

    def check_balance(self, account_no):
        account = self.find_account(account_no)
        if account is None:
            return "Account Not Found"
        return account.check_balance()

    def mini_statement(self, account_no):
        account = self.find_account(account_no)
        if account is None:
            return ["Account Not Found"]
        return file_handler.read_last_n_transactions(account.acc_no)

    def display_all_accounts(self):
        if not self.acc_store:
            return "No Accounts Available"
        return [account.account_summary() for account in self.acc_store.values()]
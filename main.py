from services.auth import AuthService
from services.bank import Bank
from services.admin import Admin
from utils import file_handler


class ByteBank:

    def __init__(self):
        self.account_store = file_handler.load_accounts_to_memory()
        self.auth = AuthService(self.account_store)
        self.bank = Bank(self.account_store)
        self.admin = Admin(self.account_store)

    def customer_menu(self, customer):

        while True:

            print("\n========== CUSTOMER MENU ==========")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Mini Statement")
            print("6. Logout")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                print(self.bank.deposit(customer.acc_no, amount))

            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                print(self.bank.withdraw(customer.acc_no, amount))

            elif choice == "3":
                recipient_acc_no = input("Enter recipient account number: ")
                amount = float(input("Enter transfer amount: "))
                print(self.bank.transfer(customer.acc_no, recipient_acc_no, amount))

            elif choice == "4":
                print(self.bank.check_balance(customer.acc_no))

            elif choice == "5":
                statement = self.bank.mini_statement(customer.acc_no)
                for line in statement:
                    print(line)

            elif choice == "6":
                print("Customer Logged Out")
                break

            else:
                print("Invalid Choice")

    def admin_menu(self):

        while True:

            print("\n========== ADMIN MENU ==========")
            print("1. Change Interest Rate")
            print("2. Change Overdraft Limit")
            print("3. Search Customer")
            print("4. View Customer")
            print("5. Block Customer")
            print("6. Unblock Customer")
            print("7. Audit Report")
            print("8. Logout")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                new_rate = float(input("Enter new interest rate: "))
                print(self.admin.change_interest_rate(new_rate))

            elif choice == "2":
                new_limit = float(input("Enter new overdraft limit: "))
                print(self.admin.change_overdraft_limit(new_limit))

            elif choice == "3":
                query = input("Enter name/email/acc_no to search: ")
                print(self.admin.search_customer(self.account_store, query))

            elif choice == "4":
                acc_no = input("Enter account number: ")
                print(self.admin.view_customer(self.account_store, acc_no))

            elif choice == "5":
                acc_no = input("Enter account number to block: ")
                print(self.admin.block_customer(self.account_store, acc_no))

            elif choice == "6":
                acc_no = input("Enter account number to unblock: ")
                print(self.admin.unblock_customer(self.account_store, acc_no))

            elif choice == "7":
                print(self.admin.audit_report(self.account_store))

            elif choice == "8":
                print("Admin Logged Out")
                break

            else:
                print("Invalid Choice")

    def start(self):

    

        while True:

            print("\n========== BYTEBANK ==========")
            print("1. Register")
            print("2. Customer Login")
            print("3. Admin Login")
            print("4. Exit")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                name = input("Name: ")
                email = input("Email: ")
                phone = input("Phone: ")
                pin = input("Set 4-digit PIN: ")
                account_type = input("Account type (savings/current): ").strip().lower()
                initial_deposit = float(input("Initial deposit: ") or 0)

                success, message, acc_no = self.auth.register(
                    name, email, phone, pin, account_type, initial_deposit
                )
                print(message)

            elif choice == "2":
                acc_no = input("Account Number: ")
                pin = input("PIN: ")

                success, message, customer = self.auth.login(acc_no, pin)
                print(message)

                if success:
                    self.customer_menu(customer)

            elif choice == "3":
                if self.admin.login():
                    self.admin.menu(list(self.account_store.values()))

            elif choice == "4":
                print("Thank You For Using ByteBank")
                break

            else:
                print("Invalid Choice")


bank = ByteBank()
bank.start()
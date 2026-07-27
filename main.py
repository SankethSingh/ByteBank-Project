from services.auth import Auth
from services.bank import Bank
from services.admin import Admin


class ByteBank:

    def __init__(self):
        self.auth = Auth()
        self.bank = Bank()
        self.admin = Admin()

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
                self.bank.deposit(customer)

            elif choice == "2":
                self.bank.withdraw(customer)

            elif choice == "3":
                self.bank.transfer(customer)

            elif choice == "4":
                self.bank.check_balance(customer)

            elif choice == "5":
                self.bank.mini_statement(customer)

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
                self.admin.change_interest_rate()

            elif choice == "2":
                self.admin.change_overdraft_limit()

            elif choice == "3":
                self.admin.search_customer(self.bank.customers)

            elif choice == "4":
                self.admin.view_customer(self.bank.customers)

            elif choice == "5":
                self.admin.block_customer(self.bank.customers)

            elif choice == "6":
                self.admin.unblock_customer(self.bank.customers)

            elif choice == "7":
                self.admin.audit_report(self.bank.customers)

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
                self.auth.register()

            elif choice == "2":

                customer = self.auth.login()

                if customer:
                    self.customer_menu(customer)

            elif choice == "3":

                if self.admin.login():
                    self.admin_menu()

            elif choice == "4":
                print("Thank You For Using ByteBank")
                break

            else:
                print("Invalid Choice")


bank = ByteBank()
bank.start()
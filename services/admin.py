from utils import file_handler

class Admin:

    def __init__(self, acc_store):
        self.acc_store = acc_store
        self.interest_rate = 5
        self.overdraft_limit = 10000

    def login(self):
        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")

        if username == "admin" and password == "admin123":
            print("Login Successful")
            return True

        print("Invalid Username or Password")
        return False

    def change_interest_rate(self, account_store):
        print("Current Interest Rate:", self.interest_rate)
        new_rate = float(input("Enter New Interest Rate: "))
        self.interest_rate = new_rate
    
        for account in account_store.values():
            if hasattr(account, "interest_rate"):
                account.interest_rate = new_rate
                file_handler.sync_account(account)
    
        print("Interest Rate Updated Successfully")

    def change_overdraft_limit(self):
        print("Current Overdraft Limit:", self.overdraft_limit)

        new_limit = float(input("Enter New Overdraft Limit: "))
        self.overdraft_limit = new_limit

        print("Overdraft Limit Updated Successfully")

    def search_customer(self, customers):
        query = input("Enter name, email, or phone to search: ").strip().lower()

        matches = [
            c for c in customers
            if query in c.name.lower() or query in c.email.lower() or query in c.phone
        ]

        if not matches:
            print("No matching customers found.")
            return

        print(f"\nFound {len(matches)} matching customer(s):")
        for customer in matches:
            print(f"- {customer.acc_no} | {customer.name} | {customer.phone} | ₹{customer.balance} | {customer.status}")


    def block_customer(self, customers):
        account_number = input("Enter Account Number: ")

        for customer in customers:
            if customer.acc_no == account_number:
                customer.status = "blocked"
                file_handler.sync_account(customer)
                print("Customer Account Blocked")
                return

        print("Customer Not Found")


    def unblock_customer(self, customers):
        account_number = input("Enter Account Number: ")

        for customer in customers:
            if customer.acc_no == account_number:
                customer.status = "active"
                file_handler.sync_account(customer)
                print("Customer Account Unblocked")
                return

        print("Customer Not Found")


    def audit_report(self, customers):
        total_balance = 0

        for customer in customers:
            total_balance = total_balance + customer.balance

        print()
        print("Bank Report")
        print("-----------")
        print("Total Customers :", len(customers))
        print("Total Balance : ₹", total_balance)

    def view_customer(self, customers):
        account_number = input("Enter Account Number: ")

        for customer in customers:
            if customer.acc_no == account_number:
                print()
                print("Customer Details")
                print("----------------")
                print("Name :", customer.name)
                print("Account Number :", customer.acc_no)
                print("Account Type :", customer.get_account_type())
                print("Phone :", customer.phone)
                print("Email :", customer.email)
                print("Balance : ₹", customer.balance)
                print("Status :", customer.status)
                print("Created Date :", customer.created_date)
                return

        print("Customer Not Found")

    def audit_report(self, customers):
        total_balance = 0

        for customer in customers:
            total_balance = total_balance + customer.balance

        print()
        print("Bank Report")
        print("-----------")
        print("Total Customers :", len(customers))
        print("Total Balance : ₹", total_balance)

    def menu(self, customers):
        while True:
        
            print()
            print("========== ADMIN MENU ==========")
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
                self.change_interest_rate()

            elif choice == "2":
                self.change_overdraft_limit()

            elif choice == "3":
                self.search_customer(customers)

            elif choice == "4":
                self.view_customer(customers)

            elif choice == "5":
                self.block_customer(customers)

            elif choice == "6":
                self.unblock_customer(customers)

            elif choice == "7":
                self.audit_report(customers)

            elif choice == "8":
                print("Logged Out")
                break
            
            else:
                print("Invalid Choice")
class EmailService:

    def __init__(self, bank_name):
        self.bank_name = bank_name

    def send_email(self, customer_name, email, transaction, amount, balance):
        print()
        print("========================================")
        print("Email Sent Successfully")
        print("========================================")
        print("To :", email)
        print("Subject : Transaction Alert")
        print()
        print("Dear", customer_name)
        print()
        print("Your transaction has been completed.")
        print("Transaction :", transaction)
        print("Amount : ", amount)
        print("Available Balance : ₹", balance)
        print()
        print("Thank you for banking with", self.bank_name)
        print("========================================")

    def deposit_email(self, customer):
        self.send_email(
            customer.name,
            customer.email,
            "Deposit",
            customer.last_amount,
            customer.balance
        )

    def withdraw_email(self, customer):
        self.send_email(
            customer.name,
            customer.email,
            "Withdrawal",
            customer.last_amount,
            customer.balance
        )

    def transfer_email(self, customer):
        self.send_email(
            customer.name,
            customer.email,
            "Money Transfer",
            customer.last_amount,
            customer.balance
        )
class Config:

    def __init__(self):

        # Bank Details
        self.bank_name = "ByteBank"

        # Default Interest Rate
        self.interest_rate = 4

        # Default Overdraft Limit
        self.overdraft_limit = 20000

        # File Names
        self.customer_file = "data/customers.csv"
        self.transaction_file = "data/transactions.csv"
        self.admin_file = "data/admin_config.json"

        # Email Details
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = "your_email@gmail.com"
        self.sender_password = "your_app_password"

    def show_bank_details(self):
        print("\n------ ByteBank Details ------")
        print("Bank Name :", self.bank_name)
        print("Interest Rate :", self.interest_rate, "%")
        print("Overdraft Limit :", self.overdraft_limit)
        print("------------------------------")
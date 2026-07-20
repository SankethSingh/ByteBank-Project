import hashlib
from datetime import datetime

class AuthService:
    def __init__(self, acc_store):
        self.acc_store = acc_store
        self.failed_attempts = {}  #acc_no -> int, in-memory only
    
    @staticmethod
    def _hash_pin(pin: str) -> str:
        return hashlib.sha256(pin.encode()).hexdigest()   #encrypt pin using SHA256 Algo
    
    # method for registration
    def register(self, name, email, phone, pin, account_type, initial_deposit=0.0, interest_rate=4.5, overdraft_limit=5000.0):

        """
        Validates input, generate unique account number, creates account subclass (Savings or Current)
        stores in memory and then to CSV. Returns (Success: bool, message: str, acc_no: str or None)
        """
        if not validator.validate_email(email):
            return False, "Invalid Email format.", None
        if not validator.validate_phone(phone):
            return False, "Invalid Phone Number format.", None
        if not validator.validate_pin(pin):
            return False, "PIN must be 4-digit number.", None
        if account_type not in ('savings', 'current'):
            return False, "Account type must be 'savings' or 'current'.", None
        if initial_deposit < 0:
            return False, "Initial deposit cannot be negative.", None
        
        acc_no = id_generator.generate_acc_no(account_type, self.acc_store)
        pin_hash = self._hash_pin(pin)
        created_date = datetime.now().strftime("%Y-%m-%d")

        if account_type == "savings":
            account = SavingsAccount(
                acc_no=acc_no, name=name, balance=initial_deposit,
                email=email, phone=phone, pin_hash=pin_hash,
                status="active", created_date=created_date,
                interest_rate=interest_rate
            )
        else:
            account = CurrentAccount(
                acc_no=acc_no, name=name, balance=initial_deposit,
                email=email, phone=phone, pin_hash=pin_hash,
                status="active", created_date=created_date,
                overdraft_limit=overdraft_limit
            )

        self.account_store[acc_no] = account
        file_handler.sync_account(account)
        file_handler.init_ledger(acc_no)

        return True, f"Account created successfully. Your account number is {acc_no}.", acc_no

    # Login 
    def login(self):
        """
        Verifies acc_no and pin against in-memory store.
        Tracks failed attempts and auto-blocks after MAX_FAILED_ATTEMPTS.
        Returns (success: bool, message: str, account: Account or None)"""

        pass

    # change pin method
    def change_pin(self):
        pass


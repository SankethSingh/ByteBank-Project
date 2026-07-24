import hashlib
from datetime import datetime

from utils import validator
from utils import id_generator
from utils import file_handler
from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount

MAX_FAILED_ATTEMPTS = 3

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
    def login(self, acc_no, pin):
        """
        Verifies acc_no and pin against in-memory store.
        Tracks failed attempts and auto-blocks after MAX_FAILED_ATTEMPTS.
        Returns (success: bool, message: str, account: Account or None)"""

        account = self.acc_store.get(acc_no)
        if account is None:
            return False, "Account number not found.", None

        if account.status == "blocked":
            return False, "This account is blocked. Contact bank administrator.", None

        if account.pin_hash != self._hash_pin(pin):
            self.failed_attempts[acc_no] = self.failed_attempts.get(acc_no, 0) + 1

            if self.failed_attempts[acc_no] >= MAX_FAILED_ATTEMPTS:
                account.status = "blocked"
                file_handler.sync_account(account)
                return False, "Too many failed attempts. Account has been blocked.", None
            remaining = MAX_FAILED_ATTEMPTS - self.failed_attempts[acc_no]
            return False, f"Incorrect PIN. {remaining} attempt(s) remaining.", None

        self.failed_attempts[acc_no] = 0 # login resets counter
        return True, "Login Successful.", account
    
    # change pin method
    def change_pin(self, acc_no, old_pin, new_pin):
        account = self.account_store.get(acc_no)
        if account is None:
            return False, "Account not found."
        if account.pin_hash != self._hash_pin(old_pin):
            return False, "Old PIN is incorrect."
        if not validator.validate_pin(new_pin):
            return False, "New PIN must be a 4-digit number."

        account.pin_hash = self._hash_pin(new_pin)
        file_handler.sync_account(account)
        return True, "PIN updated successfully."


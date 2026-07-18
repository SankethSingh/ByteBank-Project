import hashlib

class AuthService:
    def __init__(self, acc_store):
        self.acc_store = acc_store
        self.failed_attempts = {}  #acc_no -> int, in-memory only
    
    @staticmethod
    def _hash_pin(pin: str) -> str:
        return hashlib.sha256(pin.encode()).hexdigest()   #encrypt pin using SHA256 Algo
    
    # method for registration
    def register(self):
        """
        Validates input, generate unique account number, creates account subclass (Savings or Current)
        stores in memory and then to CSV. Returns (Success: bool, message: str, acc_no: str or None)
        """
        pass

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


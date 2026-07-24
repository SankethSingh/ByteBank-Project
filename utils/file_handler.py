"""
utils/file_handler.py

Storage & Communication Utilities Module (storage half).
"""

import csv
import os
from datetime import datetime

from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount

DATA_DIR = "data"
LEDGER_DIR = "ledgers"
ACCOUNTS_CSV = os.path.join(DATA_DIR, "accounts.csv")

CSV_COLUMNS = [
    "acc_no", "name", "account_type", "balance", "interest_rate",
    "overdraft_limit", "email", "phone", "pin_hash", "status", "created_date"
]


def _ensure_dirs():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(LEDGER_DIR, exist_ok=True)


def _account_to_row(account) -> dict:
    is_savings = isinstance(account, SavingsAccount)
    return {
        "acc_no": account.acc_no,
        "name": account.name,
        "account_type": "savings" if is_savings else "current",
        "balance": f"{account.balance:.2f}",
        "interest_rate": f"{account.INTEREST_RATE:.2f}" if is_savings else "0",
        "overdraft_limit": "0" if is_savings else f"{account.OVERDRAFT_LIMIT:.2f}",
        "email": account.email,
        "phone": account.phone,
        "pin_hash": account.pin_hash,
        "status": account.status,
        "created_date": account.created_date,
    }


def _row_to_account(row: dict):
    common_kwargs = dict(
        acc_no=row["acc_no"],
        name=row["name"],
        balance=float(row["balance"]),
        email=row["email"],
        phone=row["phone"],
        pin_hash=row["pin_hash"],
        status=row["status"],
        created_date=row["created_date"],
    )

    if row["account_type"] == "savings":
        return SavingsAccount(**common_kwargs, interest_rate=float(row["interest_rate"]))
    else:
        return CurrentAccount(**common_kwargs, overdraft_limit=float(row["overdraft_limit"]))


def load_accounts_to_memory() -> dict:
    """
    Reads accounts.csv (creating an empty one with headers if missing)
    and returns {acc_no: Account}. Uses DictReader so every field
    stays a plain string, avoiding numeric coercion on phone numbers.
    """
    _ensure_dirs()

    if not os.path.exists(ACCOUNTS_CSV):
        with open(ACCOUNTS_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
            writer.writeheader()
        return {}

    account_store = {}
    with open(ACCOUNTS_CSV, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            account = _row_to_account(row)
            account_store[account.acc_no] = account

    return account_store


def sync_account(account, account_store: dict = None):
    """
    Persists a single Account to accounts.csv using temp-file + os.replace
    for atomic writes. If account_store is passed, rewrites the full CSV
    from memory (safest path); otherwise patches the existing file.
    """
    _ensure_dirs()

    if account_store is not None:
        _write_all(account_store)
        return

    rows = []
    found = False
    if os.path.exists(ACCOUNTS_CSV):
        with open(ACCOUNTS_CSV, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["acc_no"] == account.acc_no:
                    rows.append(_account_to_row(account))
                    found = True
                else:
                    rows.append(row)

    if not found:
        rows.append(_account_to_row(account))

    _write_rows(rows)


def _write_all(account_store: dict):
    rows = [_account_to_row(acc) for acc in account_store.values()]
    _write_rows(rows)


def _write_rows(rows: list):
    tmp_path = ACCOUNTS_CSV + ".tmp"
    with open(tmp_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp_path, ACCOUNTS_CSV)  # atomic on POSIX and Windows


def _ledger_path(acc_no: str) -> str:
    return os.path.join(LEDGER_DIR, f"ledger_{acc_no}.txt")


def init_ledger(acc_no: str):
    _ensure_dirs()
    path = _ledger_path(acc_no)
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(f"Transaction Ledger for Account: {acc_no}\n")
            f.write("=" * 60 + "\n")


def append_ledger(acc_no: str, txn_type: str, amount: float, balance_after: float, extra: str = ""):
    _ensure_dirs()
    init_ledger(acc_no)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = (f"{timestamp} | {txn_type.upper():<10} | "
            f"Amount: {amount:>10.2f} | Balance: {balance_after:>10.2f} | {extra}\n")

    with open(_ledger_path(acc_no), "a") as f:
        f.write(line)


def read_last_n_transactions(acc_no: str, n: int = 5) -> list:
    path = _ledger_path(acc_no)
    if not os.path.exists(path):
        return []

    with open(path, "r") as f:
        lines = f.readlines()

    txn_lines = [line.strip() for line in lines[2:]]
    return txn_lines[-n:]
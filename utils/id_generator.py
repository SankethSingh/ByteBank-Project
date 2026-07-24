"""
utils/id_generator.py

Generates unique, prefixed account numbers for ByteBank.
Format: <PREFIX><6-digit sequential number>
  - SB -> Savings Account (e.g. SB100001)
  - CA -> Current Account (e.g. CA100001)
"""

PREFIX_MAP = {
    "savings": "SB",
    "current": "CA",
}

START_SEQ = 100001


def generate_acc_no(account_type: str, account_store: dict) -> str:
    """
    Generates a unique account number for the given account_type.
    Scans existing accounts in account_store to find the next free
    sequence number for that prefix, avoiding collisions even if
    savings and current accounts are numbered independently.
    """
    prefix = PREFIX_MAP.get(account_type)
    if prefix is None:
        raise ValueError(f"Unknown account_type: {account_type}")

    existing_seqs = []
    for acc_no in account_store.keys():
        if acc_no.startswith(prefix):
            try:
                existing_seqs.append(int(acc_no[len(prefix):]))
            except ValueError:
                continue

    next_seq = max(existing_seqs, default=START_SEQ - 1) + 1
    acc_no = f"{prefix}{next_seq}"

    while acc_no in account_store:
        next_seq += 1
        acc_no = f"{prefix}{next_seq}"

    return acc_no
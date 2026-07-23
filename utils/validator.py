"""
utils/validator - Regex based validation helpers used across auth, admin, and registration flows
"""

import re

EMAIL_RE = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")
PHONE_RE = re.compile(r"^(+91)?[6-9]\d{9}$")     # 10 digit number
PIN_RE = re.compile(r"\d{4}$")   # 4 digit PIN format

def validate_email(email:str) -> bool:
    return bool(EMAIL_RE.match(email or ""))

def validate_phone(phone:str) -> bool:
    return bool(PHONE_RE.match(phone or ""))

def validate_pin(pin:str) -> bool:
    return bool(PIN_RE.match(pin or ""))

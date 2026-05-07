import re

PHONE_REGEX = r'^\+989\d{9}$'

def validate_phone(phone):
    return bool(re.match(PHONE_REGEX, phone))

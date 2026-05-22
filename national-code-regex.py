import re

def validate_national_code(code):
    code = str(code).strip()
    
    if not code.isdigit() or len(code) != 10:
        return False
    
    if len(set(code)) == 1:
        return False
    
    sum = 0
    for i in range(9):
        sum += int(code[i]) * (10 - i)
    
    remainder = sum % 11
    check_digit = int(code[9])
    
    if remainder < 2:
        return check_digit == remainder
    else:
        return check_digit == 11 - remainder

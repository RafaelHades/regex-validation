import re

NATIONAL_CODE_REGEX = r'^(?!0{10})[1-9]\d{9}$'

def validate_national_code(code):
    return bool(re.match(NATIONAL_CODE_REGEX, code))
import re

NAME_REGEX = r'^[a-zA-Z\u0600-\u06FF\uFB8A\u067E\u0686\u06AF\u200C\s]+$'

def validate_name(name):
    return bool(re.match(NAME_REGEX, name))
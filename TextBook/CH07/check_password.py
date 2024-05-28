import re

def is_strong_password(password):
    length_regex = re.compile(r'.{8,}')
    upper_regex = re.compile(r'[A-Z]')
    lower_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'[0-9]')

    if (length_regex.search(password) and 
        upper_regex.search(password) and 
        lower_regex.search(password) and 
        digit_regex.search(password)):
        return True
    else:
        return False

passwords = ["WeakPass1", "strongPASS123", "Short7", "NoDigitsHere", "noUpper123", "VALID123pass"]
for pwd in passwords:
    print(f"'{pwd}': {is_strong_password(pwd)}")

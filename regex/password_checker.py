import re
#pwd pattern
pattern = re.compile(r"([A-Za-z@]{7,}[0-9]+$)")

user_pwd = input('Enter your password:')
check = pattern.fullmatch(user_pwd)
if check:
    print(f"Password validated!")
else:
    print(f"Invalid format.")





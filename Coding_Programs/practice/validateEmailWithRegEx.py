import re
def isValidEmail(email):
    regex = "^[A-Z0-9.%+-]+@[A-Z0-9]+\.[A-Z]{2,}$"
    if len(email)>7:
        if re.match(regex, email, re.IGNORECASE) is not None:
            return True

if isValidEmail("pratik0101@gmail.com"):
    print('Valid email address')
else:
    print('Invalid email address')
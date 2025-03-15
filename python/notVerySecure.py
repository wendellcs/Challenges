import string
def alphanumeric(password):
    if password == '':
        return False
    for c in password:
        if not(c in string.ascii_letters or c in string.digits):
           return False

    return True

alphanumeric("hello world_") # False
alphanumeric("PassW0rd") # True
alphanumeric("       ") # False
alphanumeric("&)))(((") # False
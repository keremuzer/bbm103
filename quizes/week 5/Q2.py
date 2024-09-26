email = input("enter your email: ")


def is_valid(email):
    if "@" in email:
        if "." in email:
            return True
        else:
            return False
    else:
        return False


print(is_valid(email))

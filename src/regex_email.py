import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+'
    #re.match function to check if email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

if __name__ == "__main__":
    email = input("Enter an email address: ")
    if is_valid_email(email):
        print("Valid email address")
    else:
        print("Invalid email address")

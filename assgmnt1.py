import string

def check_password_strength(password):
    # Criteria checks
    has_minlength = len(password) >= 8
    has_uppercase = any(ch.isupper() for ch in password)
    has_lowercase = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    special_characters = string.punctuation
    has_special = any(ch in special_characters for ch in password)

    # Checking all conditions
    if has_minlength and has_uppercase and has_lowercase and has_digit and has_special:
        return True
    else:
        return False


# ---- MAIN SCRIPT ----
password = input("Enter a password to check strength: ")

if check_password_strength(password):
    print("✔ Strong Password! Good job.")
else:
    print("✖ Weak Password! It must contain:")
    print("-- At least 8 characters")
    print("-- Uppercase and lowercase letters")
    print("-- At least one number")
    print("-- At least one special character (!,@,#,$,%,etc.)")

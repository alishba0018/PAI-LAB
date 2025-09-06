password=input("enter your password: ")
if len(password) < 8:
    print("Password is invalid: Must be at least 8 characters long.")
else:
    has_digit = False
    has_letter = False
    has_special = False
    special_chars = "@#$%"

    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isalpha():
            has_letter = True
        elif char in special_chars:
            has_special = True

    if has_digit and has_letter and has_special:
        print("Your password is valid.")
    else:
        print("Password is invalid: Must contain letters, digits, and at least one special character (@, #, $, %).")

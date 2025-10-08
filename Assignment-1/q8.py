import re

def validate_password(password):
    errors = []

    # Rule 1: Minimum length 8
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    # Rule 2: At least one uppercase letter
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter (A–Z).")

    # Rule 3: At least one lowercase letter
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter (a–z).")

    # Rule 4: At least one digit
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit (0–9).")

    # Rule 5: At least one special character from !@#$%
    if not any(char in "!@#$%" for char in password):
        errors.append("Password must contain at least one special character (!@#$%).")

    # Rule 6: No whitespaces
    if any(char.isspace() for char in password):
        errors.append("Password must not contain any whitespace characters.")

    # Return result
    if not errors:
        return True, []
    else:
        return False, errors


# --- Main Program ---
password = input("Enter your password: ")

is_valid, error_messages = validate_password(password)

print("\n--- Password Validation Result ---")
if is_valid:
    print("✅ Password is valid.")
else:
    print("❌ Password is invalid. Issues found:")
    for msg in error_messages:
        print(f"- {msg}")
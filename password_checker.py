import re


def check_password_strength(password):
    # Define criteria
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(
        r"[!@#$%^&*()\-_=+\[\]{}|;:'\",.<>?/`~\\]", password) is None

    # Assess total errors
    errors = {
        "Too short (minimum 8 characters)": length_error,
        "Missing uppercase letter": uppercase_error,
        "Missing lowercase letter": lowercase_error,
        "Missing digit": digit_error,
        "Missing special character": special_char_error,
    }

    # Print results
    if not any(errors.values()):
        print("✅ Password is Strong!")
    else:
        print("❌ Password is Weak. Issues:")
        for issue, is_error in errors.items():
            if is_error:
                print(f" - {issue}")


# Example usage
password = input("Enter your password to check: ")
check_password_strength(password)

import re

def check_password_strength(password: str) -> bool:
    """
    Function to check password strength based on security criteria.
    Criteria:
      - Minimum length 8 characters
      - At least one uppercase letter
      - At least one lowercase letter
      - At least one digit (0–9)
      - At least one special character
    Returns True if all conditions are met, else False.
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

if __name__ == "__main__":
    while True:
        password = input("Enter your password: ")
        if check_password_strength(password):
            print("✅ Strong password! Your password meets all security criteria.")
            break
        else:
            print("❌ Weak password! Please include:")
            print("- Minimum 8 characters")
            print("- At least one uppercase and one lowercase letter")
            print("- At least one number (0–9)")
            print("- At least one special character (!, @, #, $, etc.)")
            print("Please try again.\n")
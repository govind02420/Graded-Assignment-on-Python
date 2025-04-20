########## check_password_strength  ##########
import re

def check_password_strength(password):

    if len(password) < 8:                                       #Check minimum length
        return False
    
    if not re.search(r'[A-Z]', password):                       #Check for at least one uppercase letter
        return False
    
    if not re.search(r'[a-z]', password):                       #Check for at least one lowercase letter
        return False
    
    if not re.search(r'[0-9]', password):                       #Check for at least one digit
        return False
    
    if not re.search(r'[!@#$%^&*()+={}|;:",.<>?]', password):   #Check for at least one special character
        return False
    
    return True

def main():
    while True:
        password = input("Enter a password to check its strength: ")
        if check_password_strength(password):                       #Check password strength function
            print("Your password is strong.")
            break                                                   #Exit the loop
        else:
            print("""Your password is weak. Please include at least:
    - 8 characters
    - Both uppercase and lowercase letters
    - At least one digit (0-9)
    - At least one special character (e.g., !, @, #, $, %).""")

if __name__ == "__main__":
    main()
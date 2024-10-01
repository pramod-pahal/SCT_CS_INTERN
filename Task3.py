import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Length criteria
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Digits
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>).")

    # Overall assessment
    if strength == 5:
        feedback.append("Your password is strong.")
    elif strength >= 3:
        feedback.append("Your password is moderate.")
    else:
        feedback.append("Your password is weak.")

    return strength, feedback

def main():
    print("Password Strength Checker")
    while True:
        password = input("Enter a password to assess (or 'exit' to quit): ")
        if password.lower() == 'exit':
            break
        strength, feedback = assess_password_strength(password)
        print(f"Password Strength: {strength}/5")
        for comment in feedback:
            print(f"- {comment}")
        print("\n")

if __name__ == "__main__":
    main()

# This program evaluates password strength based on length.
# It checks for uppercase, lowercase, digits, and special characters,
# and also detects commonly used passwords.

import string

# A list of commonly used weak passwords
common_passwords = ["123456", "123456789", "password", "qwerty", "abc123", "password123", "admin", "admin123", "welcome",
    "letmein", "iloveyou", "monkey", "dragon", "football", "login", "user", "guest", "test123", "welcome123", "pass1234",
    "qwerty123", "123123", "000000", "111111"]

password = input("Enter password: ")

def analyze_password(password):
    score = 0

# Check if password is commonly used (weak)
    if password.lower() in common_passwords:
        return "Password leaked", 0

# Evaluate password strength based on different criteria

    if len(password) >= 8: 
        score += 20

    if any(char.isupper() for char in password):
        score += 20

    if any(char.islower() for char in password):
        score += 20

    if any(char.isdigit() for char in password):
        score += 20

    if any(char in string.punctuation for char in password):
        score += 20

# Final classification based on score

    if score <= 40:
        return "Weak", score

    elif score <= 80:
        return "Medium", score

    else:
        return "Strong", score


result, score = analyze_password(password)
print("Strength:", result, "Score:", score, "/ 100")



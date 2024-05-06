import re

def password_complexity_checker(password):
   
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    strength = 0
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    if strength == 5:
        return "Very Strong"
    elif strength >= 3:
        print(strength)
        return "Strong"
    elif strength >= 2:
        return "Moderate"
    elif strength >= 1:
        return "Weak"
    else:
        return "Very Weak"

password = input("Enter your password: ")
strength = password_complexity_checker(password)
print(f"Password strength: {strength}")

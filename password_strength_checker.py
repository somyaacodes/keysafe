"""
Password Strength Checker
--------------------------
A simple CLI tool that checks how strong a password is based on:
- Length
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of digits
- Presence of special characters

Run this file and enter a password when prompted.
"""

import re


def check_password_strength(password):
    """
    Analyzes the given password and returns a strength score (0-5)
    along with feedback on what's missing.
    """
    score = 0
    feedback = []

    # 1. Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Bonus point for longer passwords
    if len(password) >= 12:
        score += 1

    # 2. Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # 3. Lowercase letter check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # 4. Digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # 5. Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc.).")

    return score, feedback


def get_strength_label(score):
    """
    Converts a numeric score into a human-readable strength label.
    """
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"


def print_strength_bar(score, max_score=6):
    """
    Prints a simple visual bar representing the strength score.
    """
    filled = "#" * score
    empty = "-" * (max_score - score)
    print(f"[{filled}{empty}] {score}/{max_score}")


def main():
    print("=" * 40)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    while True:
        password = input("\nEnter a password to check (or 'q' to quit): ")

        if password.lower() == "q":
            print("Goodbye!")
            break

        if password == "":
            print("Please enter a password (can't be empty).")
            continue

        score, feedback = check_password_strength(password)
        label = get_strength_label(score)

        print(f"\nStrength: {label}")
        print_strength_bar(score)

        if feedback:
            print("\nSuggestions to improve:")
            for tip in feedback:
                print(f" - {tip}")
        else:
            print("\nGreat job! Your password meets all the criteria.")


if __name__ == "__main__":
    main()

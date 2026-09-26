# Password Strength Checker

A simple Python CLI tool that checks how strong your password is and tells you how to make it better.

## What it does

- Checks length, uppercase, lowercase, numbers, and special characters
- Gives your password a score out of 6
- Tells you if it's Weak, Moderate, or Strong
- Suggests what's missing

## How to run

```bash
python password_strength_checker.py
```

Type a password, hit enter, and it'll show you the result. Type `q` to quit.

## Example

```
Enter a password to check (or 'q' to quit): Test123

Strength: Moderate
[####--] 4/6

Suggestions to improve:
 - Add a special character (!@#$% etc.)
 - Try making it 12+ characters
```

## Built with

Python + regex

## Author

Somya

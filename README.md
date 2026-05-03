# Password Strength Analyzer

A Python program that demonstrates basic password strength evaluation techniques:

- Length
- Uppercase and lowercase characters
- Digits
- Special characters
- Detection of commonly used weak passwords

## Features

- Detects weak passwords from a predefined list
- Scores passwords out of 100
- Classifies passwords as Weak, Medium, or Strong

## Example

```text
Enter password: Husa!n2026
Strength: Strong | Score: 100 / 100
```
## How it works

The program evaluates a password by assigning points based on different criteria such as length, character variety (uppercase, lowercase, digits, and special characters), and whether the password appears in a list of commonly used weak passwords. The total score determines whether the password is classified as Weak, Medium, or Strong.

## Technologies Used
- Python
- String module

## Future Improvements
- Add password suggestions
- Integrate with a database of leaked passwords

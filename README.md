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

The software analyzes the strength of a password using a point system that is calculated based on various factors like the password’s length, the number of upper-case and lower-case letters, numerals, and special symbols present in the password, and finally, whether the password has been used before in a list of frequently used passwords.

## Technologies Used
- Python
- String module

## Future Improvements
- Add password suggestions
- Integrate with a database of leaked passwords

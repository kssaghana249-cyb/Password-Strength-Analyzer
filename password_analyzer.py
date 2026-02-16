import re

print("Welcome to Password Analyzer")
print("-----------------------------")

password = input("Enter your password: ")

score = 0
suggestions = []

# Length check
if len(password) >= 8:
    score += 1
else:
    suggestions.append("• Use at least 8 characters")

# Lowercase check
if re.search("[a-z]", password):
    score += 1
else:
    suggestions.append("• Add at least one lowercase letter")

# Uppercase check
if re.search("[A-Z]", password):
    score += 1
else:
    suggestions.append("• Add at least one uppercase letter")

# Number check
if re.search("[0-9]", password):
    score += 1
else:
    suggestions.append("• Add at least one number")

# Special character check
if re.search("[@#$%^&*!]", password):
    score += 1
else:
    suggestions.append("• Add at least one special character (@#$%^&*!)")

# Strength result
print("\nPassword Strength Result:")

if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")

# Print suggestions
if suggestions:
    print("\nSuggestions to improve:")
    for item in suggestions:
        print(item)

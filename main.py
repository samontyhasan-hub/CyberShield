print("Welcome to CyberShield!")
print("Password Security Analyzer")

common_passwords = [
    "password123",
    "12345678",
    "qwerty123",
    "admin123",
    "password",
    "123456789",
    "1234567890",
    "iloveyou",
    "abc12345",
    "abcd1234",
    "admin1234",
    "user1234",
    "test1234",
    "hello123",
    "welcome1",
    "pass1234",
    "qwerty1234",
    "00000000",
    "11223344",
    "11122233",
    "hello112",
    "09876543",
    "00998877",
    "11111111"
]


# Step 1: Import
import maskpass
from datetime import date

current_year = date.today().year


# Step 2: User Information
user_name = input("Enter your name (optional): ").strip()

# Birth Year Validation
while True:
    birth_year = input("Enter your birth year (optional): ").strip()

    if not birth_year:
        break

    if not birth_year.isdigit() or len(birth_year) != 4:
        print("Invalid input! Enter a 4-digit birth year.")
        continue

    birth_year_num = int(birth_year)

    if birth_year_num < current_year - 120 or birth_year_num > current_year:
        print("Invalid birth year! Please enter a valid year.")
        continue

    break


# Step 3: Password Input
password = maskpass.askpass(
    prompt="Enter password: ",
    mask="*"
)

print("Password received successfully.")


# Step 4: Personal Information Check
print("\n========== PERSONAL INFO CHECK ==========")

if user_name and user_name.lower() in password.lower():
    print("Warning: Password contains your name!")
else:
    print("Name Check: Passed")

if birth_year and str(birth_year) in password:
    print("Warning: Password contains your birth year!")
else:
    print("Birth Year Check: Passed")

if user_name and birth_year:
    if user_name.lower() in password.lower() and str(birth_year) in password:
        print("Warning: Password combines your name and birth year!")

print("=========================================")

#password input and then testing the password length
if len(password) >= 8:
    print("Length: Good")
else:
    print("Length: Too Short")

#uppercase,lowercase testing
if any(char.isupper() for char in password):
    print("Uppercase: Found")
else:
    print("Uppercase: Not Found")

if any(char.islower() for char in password):
    print("Lowercase: Found")
else:
    print("Lowercase: Not Found")

#number & special character testing
if any(char.isdigit() for char in password):
    print("Number: Found")
else:
    print("Number: Not Found")

if any(not char.isalnum() for char in password):
    print("Special Character: Found")
else:
    print("Special Character: Not Found")


#Password Strength Calculation

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(not char.isalnum() for char in password):
    score += 1

print("Password Score:", score, "/5")
if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

percentage = (score / 5) * 100

print("Password Strength:", percentage, "%")


#Final RESULT

print("\n===== CYBERSHIELD REPORT =====")
print("Password Length:", len(password))
print("Security Score:", score, "/5")
print("Security Percentage:", percentage, "%")
print("Final Result:", "Weak" if score <= 2 else "Medium" if score <= 4 else "Strong")
print("==============================")

#common password testing

if password.lower() in common_passwords:
    print("Warning: This is a common password!")
else:
    print("Common Password Check: Passed")

#password feedback

print("\n========== PASSWORD FEEDBACK ==========")

suggestions = []

if len(password) < 8:
    suggestions.append("Use at least 8 characters.")

if not any(char.isupper() for char in password):
    suggestions.append("Add uppercase letters (A-Z).")

if not any(char.islower() for char in password):
    suggestions.append("Add lowercase letters (a-z).")

if not any(char.isdigit() for char in password):
    suggestions.append("Include numbers (0-9).")

if not any(not char.isalnum() for char in password):
    suggestions.append("Include special characters.")

if password.lower() in common_passwords:
    suggestions.append("Avoid common password patterns.")

if suggestions:
    print("Suggestions to improve your password:")
    for item in suggestions:
        print("-", item)
else:
    print("All basic checks passed!")

print("=======================================")


#security check

print("\n========== SECURITY CHECKLIST ==========")

checks = {
    "Minimum 8 Characters": len(password) >= 8,
    "Uppercase Letter": any(char.isupper() for char in password),
    "Lowercase Letter": any(char.islower() for char in password),
    "Number": any(char.isdigit() for char in password),
    "Special Character": any(not char.isalnum() for char in password)
}

for check, result in checks.items():
    if result:
        print("[PASS]", check)
    else:
        print("[FAIL]", check)

print("========================================")

#password risk warning

print("\n========== RISK ANALYSIS ==========")

risks = []

weak_patterns = [
    "123",
    "234",
    "345",
    "321",
    "abc",
    "bcd",
    "cde",
    "cba",
    "qwerty",
    "567",
    "765",
    "987",
    "789"
]

if any(pattern in password.lower() for pattern in weak_patterns):
    risks.append("Password contains a predictable sequence.")

if len(password) < 8:
    risks.append("Password is too short.")

if password.isalpha():
    risks.append("Password contains only letters.")

if password.isdigit():
    risks.append("Password contains only numbers.")

if password.lower() in common_passwords:
    risks.append("Password is commonly used.")

if len(set(password)) == 1:
    risks.append("Password contains only repeated characters.")

if risks:
    print("Potential Risks Found:")
    for risk in risks:
        print("-", risk)
else:
    print("No obvious risks detected.")

print("===================================")

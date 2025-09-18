import re

def check_strength(password):
    strength = 0
    remarks = ""

    if len(password) < 6:
        remarks = "Too short. Use at least 8 characters."
    elif len(password) >= 8:
        strength += 1

    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    levels = {1: "Weak 😢", 2: "Fair 😐", 3: "Good 🙂", 4: "Strong 💪", 5: "Very Strong 🔥"}
    return levels.get(strength, "Very Weak")

if __name__ == "__main__":
    password = input("Enter your password: ")
    print("Password Strength:", check_strength(password))

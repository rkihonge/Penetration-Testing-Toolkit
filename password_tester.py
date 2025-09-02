import re

def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Password too short (min 8 chars required).")
    if not re.search(r"[A-Z]", password):
        issues.append("Missing uppercase letter.")
    if not re.search(r"[a-z]", password):
        issues.append("Missing lowercase letter.")
    if not re.search(r"[0-9]", password):
        issues.append("Missing digit.")
    if not re.search(r"[@$!%*?&#]", password):
        issues.append("Missing special character.")

    if not issues:
        return "Strong password."
    else:
        return "Weak password:\n" + "\n".join(issues)

if __name__ == "__main__":
    pwd = input("Enter password to test: ")
    result = check_password_strength(pwd)
    print(result)
    with open("sample_report.txt", "a") as f:
        f.write(f"Password Test: {result}\n")

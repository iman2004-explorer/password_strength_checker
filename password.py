import re
import tkinter as tk
from tkinter import messagebox

def check_password():
    password = entry.get()

    
    length_ok = len(password) >= 8
    upper_ok = re.search(r"[A-Z]", password)
    lower_ok = re.search(r"[a-z]", password)
    digit_ok = re.search(r"[0-9]", password)
    special_ok = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([length_ok, bool(upper_ok), bool(lower_ok), bool(digit_ok), bool(special_ok)])

    if score == 5:
        strength = "Strong"
        color = "green"
    elif score >= 3:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    result_label.config(text=f"Strength: {strength}", fg=color)

    details = ""
    if not length_ok: details += "- Minimum 8 characters\n"
    if not upper_ok: details += "- At least one uppercase letter\n"
    if not lower_ok: details += "- At least one lowercase letter\n"
    if not digit_ok: details += "- At least one number\n"
    if not special_ok: details += "- At least one special character\n"

    if details:
        messagebox.showwarning("Requirements Missing", details)
    else:
        messagebox.showinfo("Password Status", "Your password is strong!")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.config(bg="#f2f2f2")

title = tk.Label(root, text="Password Checker", font=("Arial", 18, "bold"), bg="#f2f2f2")
title.pack(pady=10)

entry = tk.Entry(root, show="*", font=("Arial", 14), width=25)
entry.pack(pady=10)

check_btn = tk.Button(root, text="Check Password", command=check_password, font=("Arial", 12))
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f2f2f2")
result_label.pack(pady=10)

root.mainloop()

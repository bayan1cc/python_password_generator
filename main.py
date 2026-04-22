import random
import tkinter as tk
from tkinter import messagebox

chars_list = [
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "!@#$%^&*()-_=+[]{}|;:,.<>?/"
]

def random_char():
    group = random.choice(chars_list)
    return random.choice(group)

def generate_password():
    try:
        length = int(entry.get())

        if length <= 0:
            raise ValueError

        password = ""
        for _ in range(length):
            password += random_char()

        shuffled_password = "".join(random.sample(password, len(password)))

        result_label.config(text=f"Your password: {shuffled_password}")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid positive number!")



# --- GUI ---
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x200")

tk.Label(root, text="Password length:").pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generate", command=generate_password).pack(pady=10)

result_label = tk.Label(root, text="Your password will appear here")
result_label.pack(pady=10)

root.mainloop()


import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            result_label.config(text="Password length must be at least 4")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
        copy_btn.config(state="normal")
    except ValueError:
        result_label.config(text="Enter a valid number")
        copy_btn.config(state="disabled")

def copy_password():
    password = result_label.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        copy_btn.config(text="Copied")
        root.after(1500, lambda: copy_btn.config(text="Copy Password"))

root = tk.Tk()
root.title("Password Generator")
root.geometry("420x280")
root.config(bg="#1e1e1e")

title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), fg="white", bg="#1e1e1e")
title_label.pack(pady=15)

length_label = tk.Label(root, text="Enter Password Length:", font=("Arial", 12), fg="white", bg="#1e1e1e")
length_label.pack()

length_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
length_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#0078D7", fg="white",
                         command=generate_password, cursor="hand2")
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Consolas", 12), fg="#00FF7F", bg="#1e1e1e", wraplength=380)
result_label.pack(pady=10)

copy_btn = tk.Button(root, text="Copy Password", font=("Arial", 11, "bold"), bg="#444", fg="white",
                     state="disabled", command=copy_password, cursor="hand2")
copy_btn.pack(pady=5)

root.mainloop()

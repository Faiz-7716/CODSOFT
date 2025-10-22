import customtkinter as ctk
import math

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("360x640")
app.title("Calculator _ Project")

entry_frame = ctk.CTkFrame(app, fg_color="#000000", corner_radius=12)
entry_frame.pack(padx=15, pady=20, fill="x")

input_var = ctk.StringVar()
output_var = ctk.StringVar()

input_label = ctk.CTkLabel(entry_frame, textvariable = input_var,
                           font = ("Segoe UI", 24), anchor="e",
                           text_color="#ffffff", height=50)
input_label.pack(padx=12, pady=(12,4), fill="x")
output_label = ctk.CTkLabel(entry_frame, textvariable = output_var,
                            font = ("Segoe UI", 24, "bold"), anchor="e",
                            text_color="#ffffff", height=60)
output_label.pack(padx=12, pady=(0,12), fill="x")

def press(key):
    if key == "=":
        try:
            expression = input_var.get().replace("^", "**")
            result = eval(expression)
            output_var.set(str(round(result, 6)))
        except ZeroDivisionError:
            output_var.set("Div By Zero")
        except :
            output_var.set("Error")
    elif key == "c":
        input_var.set("")
        output_var.set("")
    elif key == "del":
        input_var.set(input_var.get()[:-1])
    elif key == "√":
        try:
            value = float(input_var.get())
            output_var.set(str(round(math.sqrt(value),6)))
        except :
            output_var.set("Error")

    elif key == "log":
        try:
            value = float(input_var.get())
            output_var.set(str(round(math.log10(value),6)))
        except :
            output_var.set("Error")
    else:
        input_var.set(input_var.get() + key)

btn_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
btn_frame.pack(padx=10, pady=0, fill="both", expand=True)

buttons = [
    [
    "c", "del", "%", "/"
    ],
    [
    "7", "8", "9", "*"
    ],
    [
    "4", "5", "6", "-"
    ],
    [
    "1", "2", "3", "+"
    ],
    [
    "0", ".", "^", "="
    ]
]

def crete_button(txt, row, col):
    color = "#FF9500" if txt ==  "=" else "#2e2e2e"
    button = ctk.CTkButton(
        btn_frame, text=txt, corner_radius=100,
        fg_color=color,
        hover_color="#555555",
        font = ("Segoe UI", 20, "bold"),
        text_color="#ffffff",
        command = lambda: press(txt)
    )
    button.grid( row = row, column = col, sticky="nsew", padx=5, pady=5)

for r, row_vals in enumerate(buttons):
    for c, char in enumerate(row_vals):
        crete_button(char, r, c)

for i in range(5):
    btn_frame.rowconfigure(i, weight=1)
for j in range(4):
    btn_frame.columnconfigure(j, weight=1)
app.mainloop()
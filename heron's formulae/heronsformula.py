import tkinter as tk
from tkinter import messagebox
import math

def calculate_area():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for all sides.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Triangle Area Calculator")

bg_color = "#2e2e2e"
fg_color = "#ffffff"
entry_bg_color = "#3e3e3e"
root.configure(bg=bg_color)

tk.Label(root, text="Side a:", bg=bg_color, fg=fg_color).grid(row=0, column=0, padx=10, pady=5)
entry_a = tk.Entry(root, bg=entry_bg_color, fg=fg_color, insertbackground=fg_color)
entry_a.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Side b:", bg=bg_color, fg=fg_color).grid(row=1, column=0, padx=10, pady=5)
entry_b = tk.Entry(root, bg=entry_bg_color, fg=fg_color, insertbackground=fg_color)
entry_b.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Side c:", bg=bg_color, fg=fg_color).grid(row=2, column=0, padx=10, pady=5)
entry_c = tk.Entry(root, bg=entry_bg_color, fg=fg_color, insertbackground=fg_color)
entry_c.grid(row=2, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area, bg=entry_bg_color, fg=fg_color)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Area: ", bg=bg_color, fg=fg_color)
result_label.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
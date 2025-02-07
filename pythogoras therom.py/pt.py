import tkinter as tk

def solve():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = (a**2 + b**2) ** 0.5
        result_label.config(text=f"c = {c:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

root = tk.Tk()
root.title("Pythagorean Theorem Solver")
root.geometry("300x150")

# Labels for the input fields
a_label = tk.Label(root, text="Length of side a:")
b_label = tk.Label(root, text="Length of side b:")
c_label = tk.Label(root, text="Hypotenuse (c):")

a_label.pack(anchor='w')
b_label.pack(anchor='w')
result_label = tk.Label(root, text="Calculating...", font=('Arial', 12, 'italic'))
result_label.pack(anchor='w')

# Input fields
a_entry = tk.Entry(root)
b_entry = tk.Entry(root)

a_entry.pack(anchor='w')
b_entry.pack(anchor='w')

# Solve button
solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.pack()

root.mainloop()
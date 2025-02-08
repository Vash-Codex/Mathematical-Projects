import tkinter as tk
from tkinter import messagebox
import math

def calculate_area():
    """Calculate the area of a circle using the provided radius."""
    try:
        # Retrieve the radius from the entry widget and convert it to a float
        radius = float(radius_entry.get())
        if radius < 0:
            # Show an error if the radius is negative
            messagebox.showerror("Input Error", "Radius cannot be negative.")
            return
        
        # Calculate the area
        area = math.pi * radius ** 2
        
        # Update the result label with the calculated area
        result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        # Show an error if the input is not a valid number
        messagebox.showerror("Input Error", "Please enter a valid number for the radius.")

# Create the main window
root = tk.Tk()
root.title("Circle Area Calculator")
root.geometry("300x150")  # Optional: Set a fixed window size

# Create and place the widgets

# Label for the radius entry
radius_label = tk.Label(root, text="Enter radius:")
radius_label.pack(pady=(10, 0))

# Entry widget for the user to input the radius
radius_entry = tk.Entry(root)
radius_entry.pack(pady=5)

# Button to trigger the area calculation
calc_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calc_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="Area:")
result_label.pack(pady=(5, 10))

# Start the Tkinter event loop
root.mainloop()

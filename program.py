import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style, PRIMARY, SUCCESS
from PIL import Image, ImageTk

def convert():
    try:
        value = float(input_entry.get())
        from_unit = from_combo.get()
        to_unit = to_combo.get()
        
        if from_unit == to_unit:
            result = value
        elif from_unit == "Celsius":
            if to_unit == "Kelvin":
                result = value + 273.15
            else:  # Fahrenheit
                result = (value * 9/5) + 32
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = value - 273.15
            else:  # Fahrenheit
                result = (value - 273.15) * 9/5 + 32
        else:  # From Fahrenheit
            if to_unit == "Celsius":
                result = (value - 32) * 5/9
            else:  # Kelvin
                result = (value - 32) * 5/9 + 273.15
        
        output_entry.config(state="normal")
        output_entry.delete(0, tk.END)
        output_entry.insert(0, f"{result:.2f}")
        output_entry.config(state="readonly")
        update_status("Conversion successful!", SUCCESS)
    except ValueError:
        update_status("Please enter a valid number", PRIMARY)

def reset():
    input_entry.delete(0, tk.END)
    output_entry.config(state="normal")
    output_entry.delete(0, tk.END)
    output_entry.config(state="readonly")
    from_combo.set("Celsius")
    to_combo.set("Kelvin")
    clear_status()

def update_status(message, style):
    status_label.config(text=message, bootstyle=(style, "inverse"))

def clear_status():
    status_label.config(text="", bootstyle="default")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x350")
root.resizable(False, False)

# Use ttkbootstrap style
style = Style(theme="flatly")

# Custom style for Combobox
style.configure("TCombobox", foreground="black", background="white")
style.map("TCombobox", fieldbackground=[("readonly", "white")], selectbackground=[("readonly", "#0078D7")])

# Load and set icon
try:
    icon = Image.open("icon/temperature.png")
    photo = ImageTk.PhotoImage(icon)
    root.iconphoto(False, photo)
except:
    print("Icon file not found")

# Create main frame
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Create and arrange widgets
input_label = ttk.Label(main_frame, text="Enter temperature:", font=("Helvetica", 12))
input_label.grid(row=0, column=0, sticky="w", pady=5)

input_entry = ttk.Entry(main_frame, width=15, font=("Helvetica", 12))
input_entry.grid(row=0, column=1, sticky="we", pady=5)

from_label = ttk.Label(main_frame, text="From unit:", font=("Helvetica", 12))
from_label.grid(row=1, column=0, sticky="w", pady=5)

units = ["Celsius", "Kelvin", "Fahrenheit"]
from_combo = ttk.Combobox(main_frame, values=units, width=13, font=("Helvetica", 12), state="readonly", style="TCombobox")
from_combo.set("Celsius")
from_combo.grid(row=1, column=1, sticky="we", pady=5)

to_label = ttk.Label(main_frame, text="To unit:", font=("Helvetica", 12))
to_label.grid(row=2, column=0, sticky="w", pady=5)

to_combo = ttk.Combobox(main_frame, values=units, width=13, font=("Helvetica", 12), state="readonly", style="TCombobox")
to_combo.set("Kelvin")
to_combo.grid(row=2, column=1, sticky="we", pady=5)

convert_btn = ttk.Button(main_frame, text="Convert", command=convert, style="success.TButton")
convert_btn.grid(row=3, column=0, columnspan=2, sticky="we", pady=10)

output_label = ttk.Label(main_frame, text="Result:", font=("Helvetica", 12))
output_label.grid(row=4, column=0, sticky="w", pady=5)

output_entry = ttk.Entry(main_frame, width=15, font=("Helvetica", 12), state="readonly")
output_entry.grid(row=4, column=1, sticky="we", pady=5)

reset_btn = ttk.Button(main_frame, text="Reset", command=reset, style="secondary.TButton")
reset_btn.grid(row=5, column=0, columnspan=2, sticky="we", pady=10)

status_label = ttk.Label(main_frame, text="", font=("Helvetica", 10))
status_label.grid(row=6, column=0, columnspan=2, sticky="we", pady=5)

# Adjust column size
main_frame.columnconfigure(1, weight=1)

root.mainloop()
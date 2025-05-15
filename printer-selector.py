import tkinter as tk
from tkinter import ttk, messagebox

# Dummy printer list
printers = [
    "HP LaserJet Pro M404dn",
    "Canon Pixma G6020",
    "Epson EcoTank ET-2760",
    "Brother HL-L2390DW"
]

def print_selected():
    selected_printer = printer_var.get()
    sides = sides_var.get()
    messagebox.showinfo("Print Job", f"Sending to printer: {selected_printer}\nSides: {sides}")

root = tk.Tk()
root.title("Printer Selector")
root.geometry("400x200")

tk.Label(root, text="Select Printer:").pack(pady=5)
printer_var = tk.StringVar()
printer_menu = ttk.Combobox(root, textvariable=printer_var, values=printers, state="readonly")
printer_menu.current(0)
printer_menu.pack(pady=5)

tk.Label(root, text="Print Sides:").pack(pady=5)
sides_var = tk.StringVar(value="1-side")
tk.Radiobutton(root, text="1-side", variable=sides_var, value="1-side").pack()
tk.Radiobutton(root, text="2-side", variable=sides_var, value="2-side").pack()

tk.Button(root, text="Print", command=print_selected).pack(pady=10)

root.mainloop()

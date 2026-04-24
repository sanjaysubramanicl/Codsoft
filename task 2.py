import tkinter as tk
from tkinter import messagebox
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operation.get()
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            messagebox.showwarning("Warning", "Please select an operation!")
            return
        messagebox.showinfo("Result", f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")
tk.Label(root, text="Calculator", font=("Arial", 16)).pack(pady=10)
tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()
tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()
operation = tk.StringVar()
tk.Label(root, text="Select Operation").pack()
tk.Radiobutton(root, text="Addition (+)", variable=operation, value="+").pack()
tk.Radiobutton(root, text="Subtraction (-)", variable=operation, value="-").pack()
tk.Radiobutton(root, text="Multiplication (*)", variable=operation, value="*").pack()
tk.Radiobutton(root, text="Division (/)", variable=operation, value="/").pack()
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)
root.mainloop()
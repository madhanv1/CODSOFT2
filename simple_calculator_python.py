import tkinter as tk

# Function to perform calculation
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(entry.get())  # Evaluate the expression in the entry box
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the input and result
entry = tk.Entry(root, width=25, font=("Arial", 14), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('C', 4, 0), ('=', 4, 2)
]

# Create and place buttons on the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=calculate_result)
    elif text == "C":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=clear_entry)
    else:
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=lambda value=text: click_button(value))
    
    button.grid(row=row, column=col)

# Start the main event loop
root.mainloop()

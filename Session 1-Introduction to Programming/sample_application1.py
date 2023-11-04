import tkinter as tk

# Create a function to perform the arithmetic operation
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operator = operator_var.get()

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error (Division by zero)"

    label_result.config(text="Result: " + str(result))

# Create the main application window
app = tk.Tk()
app.title("Basic Calculator")

# Create data: Input fields and operator choices
label_num1 = tk.Label(app, text="Enter first number:")
entry_num1 = tk.Entry(app)
label_num2 = tk.Label(app, text="Enter second number:")
entry_num2 = tk.Entry(app)

operator_var = tk.StringVar()
operator_var.set("+")  # Default operator is addition

label_operator = tk.Label(app, text="Select operator:")
operator_choices = ["+", "-", "*", "/"]
operator_menu = tk.OptionMenu(app, operator_var, *operator_choices)

# Create a button to trigger the calculation process
calculate_button = tk.Button(app, text="Calculate", command=calculate)

# Create data: Output field to display the result
label_result = tk.Label(app, text="Result: ")

# Create a basic layout for the GUI
label_num1.pack()
entry_num1.pack()
label_num2.pack()
entry_num2.pack()
label_operator.pack()
operator_menu.pack()
calculate_button.pack()
label_result.pack()

# Start the GUI application
app.mainloop()

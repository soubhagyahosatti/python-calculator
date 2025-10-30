# ------------------------------------------------------------
# Mini Project: Calculator App
# Created using Python and Tkinter (built-in GUI library)
# ------------------------------------------------------------

import tkinter as tk

# Global variable to store the expression (ex: "7+8*2")
expression = ""

# Function to handle button press (numbers/operators)
def press(num):
    """
    This function adds the pressed button (number/operator)
    to the expression and updates the display field.
    """
    global expression
    expression += str(num)         # Add number/operator to expression
    equation.set(expression)       # Update display

# Function to evaluate the final result
def equalpress():
    """
    This function evaluates the arithmetic expression
    and shows the result in the display.
    """
    try:
        global expression
        total = str(eval(expression))   # eval() calculates the expression
        equation.set(total)             # Show result
        expression = total              # Keep result for further use
    except:
        equation.set("Error")           # Handle invalid input
        expression = ""                 # Reset expression

# Function to clear the display
def clear():
    """
    Clears the expression and resets the display field.
    """
    global expression
    expression = ""
    equation.set("")

# Function to delete last character (Backspace)
def backspace():
    """
    Deletes the last entered character (like ⌫).
    """
    global expression
    expression = expression[:-1]
    equation.set(expression)

# ------------------------------------------------------------
# Main GUI code
# ------------------------------------------------------------
if __name__ == "__main__":
    # Create main window
    gui = tk.Tk()
    gui.title("Calculator App")
    gui.configure(bg="black")
    gui.geometry("360x550")
    gui.resizable(False, False)   # Fix window size

    # StringVar() is used to update the display
    equation = tk.StringVar()

    # Entry field (Display screen)
    entry_field = tk.Entry(
        gui, textvariable=equation, font=('Arial', 28, 'bold'),
        bd=0, insertwidth=2, width=15,
        bg="black", fg="white", justify="right"
    )
    entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, pady=10)

    # --------------------------------------------------------
    # Function to create buttons easily
    # --------------------------------------------------------
    def create_button(text, row, col, bg="#333333", fg="white", cmd=None, colspan=1):
        """
        Creates a calculator button and places it in the grid.
        """
        if cmd is None:
            cmd = lambda: press(text)   # Default action is to add text to expression
        b = tk.Button(gui, text=text, command=cmd,
                      font=('Arial', 20), fg=fg, bg=bg,
                      bd=0, relief="ridge",
                      width=5, height=2)
        b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3)

    # --------------------------------------------------------
    # Button Layout
    # --------------------------------------------------------
    create_button("AC", 1, 0, bg="red", cmd=clear)        # All Clear
    create_button("⌫", 1, 1, bg="#ff9500", cmd=backspace) # Backspace
    create_button("%", 1, 2, bg="#ff9500")                # Modulus
    create_button("÷", 1, 3, bg="#ff9500", cmd=lambda: press("/"))

    create_button("7", 2, 0)
    create_button("8", 2, 1)
    create_button("9", 2, 2)
    create_button("×", 2, 3, bg="#ff9500", cmd=lambda: press("*"))

    create_button("4", 3, 0)
    create_button("5", 3, 1)
    create_button("6", 3, 2)
    create_button("-", 3, 3, bg="#ff9500")

    create_button("1", 4, 0)
    create_button("2", 4, 1)
    create_button("3", 4, 2)
    create_button("+", 4, 3, bg="#ff9500")

    create_button("0", 5, 0, colspan=2)   # Wide zero button
    create_button(".", 5, 2)
    create_button("=", 5, 3, bg="#ff9500", cmd=equalpress)

    # --------------------------------------------------------
    # Run the app
    # --------------------------------------------------------
    gui.mainloop()
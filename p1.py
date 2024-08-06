from tkinter import Tk, Entry , Button, StringVar

class Calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="gray")
        master.resizable(False,False)

        self.equation=StringVar()
        self.entry_value=''
        Entry(width=17,bg='#fff',font=("Arial Bold",28),textvariable=self.equation).place(x=0,y=0)

    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)

    def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)

# Initialize the main application window
root =Tk()

# Create an instance of the Calculator class and pass the root window to it
calculator = Calculator(root)

# Run the Tkinter event loop
root.mainloop()

# import tkinter as tk

# class Calculator:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Calculator")
        
#         self.entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=2)
#         self.entry.grid(row=0, column=0, columnspan=4)
        
#         self.create_buttons()

#     def create_buttons(self):
#         buttons = [
#             '(', ')', '%', '/',
#             '1', '2', '3', '*',
#             '4', '5', '6', '-',
#             '7', '8', '9', '+',
#             'c', '0', '.', '=',
#         ]

#         row_val = 1
#         col_val = 0

#         for button in buttons:
#             command = lambda x=button: self.on_button_click(x)
#             tk.Button(self.root, text=button, width=10, height=3, command=command).grid(row=row_val, column=col_val)
#             col_val += 1
#             if col_val > 3:
#                 col_val = 0
#                 row_val += 1

#     def on_button_click(self, char):
#         current_text = self.entry.get()
#         if char == '=':
#             try:
#                 result = str(eval(current_text))
#                 self.entry.delete(0, tk.END)
#                 self.entry.insert(tk.END, result)
#             except Exception as e:
#                 self.entry.delete(0, tk.END)
#                 self.entry.insert(tk.END, "Error")
#         else:
#             self.entry.insert(tk.END, char)

# # Initialize the main application window
# root = tk.Tk()

# # Create an instance of the Calculator class and pass the root window to it
# calculator = Calculator(root)

# # Run the Tkinter event loop
# root.mainloop()

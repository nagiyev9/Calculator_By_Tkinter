import math
import ttkbootstrap as ttk
import tkinter as tk

class App(ttk.Window):

    def __init__(self):
        super().__init__(title="Calculator", iconphoto="logo-icon.png")

        # Window size parameters
        app_min_width = 500
        app_min_height = 550

        middle_x = self.winfo_screenwidth() // 2 - app_min_width // 2
        middle_y = self.winfo_screenheight() // 2 - app_min_height // 2

        self.geometry(f"{app_min_width}x{app_min_height}+{middle_x}+{middle_y}")
        self.resizable(width=False, height=False)

        # Input
        self.input = ttk.Entry(self, font=('Arial', 22))
        self.input.pack(fill=tk.X, padx=10, pady=10)
        self.input.focus_set()

        # Buttons' Frame
        self.frame = ttk.Frame(self, padding=10)
        self.frame.pack(fill=tk.BOTH, expand=True) 

        # Grid configuration
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_columnconfigure(3, weight=1)
        self.frame.grid_columnconfigure(4, weight=1) 
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_rowconfigure(3, weight=1)

        # First row of buttons
        tk.Button(self.frame, text="7", width=10, height=5, command=lambda: self.action("7")).grid(row=0, column=0, sticky='nsew')
        tk.Button(self.frame, text="8", width=10, height=5, command=lambda: self.action("8")).grid(row=0, column=1, sticky='nsew')
        tk.Button(self.frame, text="9", width=10, height=5, command=lambda: self.action("9")).grid(row=0, column=2, sticky='nsew')
        tk.Button(self.frame, text="/", width=10, height=5, command=lambda: self.action("/")).grid(row=0, column=3, sticky='nsew')
        tk.Button(self.frame, text="AC", width=10, height=5, command=lambda: self.clear()).grid(row=0, column=4, sticky='nsew')

        # Second row of buttons
        tk.Button(self.frame, text="4", width=10, height=5, command=lambda: self.action("4")).grid(row=1, column=0, sticky='nsew')
        tk.Button(self.frame, text="5", width=10, height=5, command=lambda: self.action("5")).grid(row=1, column=1, sticky='nsew')
        tk.Button(self.frame, text="6", width=10, height=5, command=lambda: self.action("6")).grid(row=1, column=2, sticky='nsew')
        tk.Button(self.frame, text="x", width=10, height=5, command=lambda: self.action("*")).grid(row=1, column=3, sticky='nsew')
        tk.Button(self.frame, text="x²", width=10, height=5, command=lambda: self.action("x²")).grid(row=1, column=4, sticky='nsew')

        # Third row of buttons
        tk.Button(self.frame, text="1", width=10, height=5, command=lambda: self.action("1")).grid(row=2, column=0, sticky='nsew')
        tk.Button(self.frame, text="2", width=10, height=5, command=lambda: self.action("2")).grid(row=2, column=1, sticky='nsew')
        tk.Button(self.frame, text="3", width=10, height=5, command=lambda: self.action("3")).grid(row=2, column=2, sticky='nsew')
        tk.Button(self.frame, text="-", width=10, height=5, command=lambda: self.action("-")).grid(row=2, column=3, sticky='nsew')

        # Fourth row of buttons
        tk.Button(self.frame, text="0", width=10, height=5, command=lambda: self.action("0")).grid(row=3, column=0, sticky='nsew')
        tk.Button(self.frame, text=".", width=10, height=5, command=lambda: self.action(".")).grid(row=3, column=1, sticky='nsew')
        tk.Button(self.frame, text="%", width=10, height=5, command=lambda: self.action("%")).grid(row=3, column=2, sticky='nsew')
        tk.Button(self.frame, text="+", width=10, height=5, command=lambda: self.action("+")).grid(row=3, column=3, sticky='nsew')

        tk.Button(self.frame, text="=", width=10, height=10, command=lambda: self.equals()).grid(row=2, column=4, rowspan=2, sticky='nsew')

    def action(self, arg):
        self.input.insert(tk.END, arg)

    def equals(self):
        try:
            self.value = self.input.get()

            if 'x²' in self.value:
                try:
                    self.value_list = self.value.split('x²')

                    try:
                        result = math.pow(float(self.value_list[0]), float(self.value_list[1]))
                        self.input.delete(0, tk.END)
                        self.input.insert(0, str(result))
                    except ValueError:
                        self.input.delete(0, tk.END)
                        self.input.insert(0, 'Error')
                except ValueError:
                    self.input.delete(0, tk.END)
                    self.input.insert(0, 'Error')
            else:
                self.value = eval(self.value)
                self.input.delete(0, tk.END)
                self.input.insert(0, str(self.value))

        except SyntaxError or NameError:
            self.input.delete(0, tk.END)
            self.input.insert(0, 'Error')

    def clear(self):
        self.input.delete(0, tk.END)

    def square(self):
        try:
            self.value = self.input.get()
        except SyntaxError or NameError:
            self.input.delete(0, tk.END)
            self.input.insert(0, 'Error')
        else:
            self.value_list = self.value.split('x²')
            math.pow(self.value_list[0], self.value_list[1])
            self.input.delete(0, tk.END)
            self.input.insert(0, self.value)


# App
app = App()
app.mainloop()
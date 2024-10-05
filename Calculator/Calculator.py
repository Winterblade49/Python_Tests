import tkinter as tk
import _json

Calc_Width = 250
Calc_Height = 400

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        # Create a label
        self.label = tk.Label(self, text="This is a label")
        self.label.pack()
        
        # Create a button
        self.button = tk.Button(self, text="1", command=self.button_clicked)
        self.button.pack()

    def button_clicked(self):
        print("Button clicked!")

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("Calculator")
myapp.master.minsize(Calc_Width, Calc_Height)
myapp.master.maxsize(Calc_Width, Calc_Height)

#change window Icon
myapp.master.iconbitmap('Images/Calculator Icon.png')

# start the program
myapp.mainloop()













import tkinter as tk
import _json

Calc_Width = 250
Calc_Height = 400

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        
        # Create a button
        self.button = tk.Button(self, text="1", command=self.button_clicked1)
        self.button.pack()
        
    def button_clicked1(self):
        print("Button 1 clicked!")
        
        
        # create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("Calculator")
myapp.master.minsize(Calc_Width, Calc_Height)
myapp.master.maxsize(Calc_Width, Calc_Height)

#change window Icon
myapp.master.iconbitmap('Calculator/Images/Calculator_Icon.ico')

# start the program
myapp.mainloop()


class Calc_Button(App):
    def __init__(self):
        print ("Button")
        

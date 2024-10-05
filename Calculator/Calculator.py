import tkinter as tk
import json

Calc_Width = 250
Calc_Height = 400

class Calc_Buttons(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
    def Create_button(self,Button_Name,Button_Command):
        # Creates a button
        self.button = tk.Button(self, text=Button_Name, command= lambda name=Button_Name: self.button_clicked(name))
        self.button.pack()
    
    def button_clicked(self,name):
        print(name)
            



class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        #def instance od Calc buttons class
        Buttons = Calc_Buttons(self)

        #creates all 9 number buttons
        for i in range(0,10,1):
            Buttons.Create_button(i,Buttons.button_clicked)
            
        #creates all operand buttons   
        Operands = ("x","y","-","+",)    
        for value in Operands:
            Buttons.Create_button(value,Buttons.button_clicked)
        
        

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


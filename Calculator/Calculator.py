import tkinter as tk
import json

Calc_Width = 250
Calc_Height = 400



class Calc_Buttons(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()  
        
    def Create_button(self,Button_Name,row=0,colum=0,button_size=2):
        # Creates a button
        self.button = tk.Button(self, text=Button_Name, command= lambda name=Button_Name: self.button_clicked(name),font=("Helvetica", button_size),width=2)
        self.button.grid(row=row,column=colum)


    
    def button_clicked(self,name):
        print(name)
            



class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        # Create an input field at the top
        self.input_field = tk.Entry(self, width=10, font=("Helvetica", 24))
        self.input_field.pack(side=tk.TOP)
        
        
        #def instance od Calc buttons class
        Buttons = Calc_Buttons(self)

        #creates all 9 number buttons
        for i in range(0,10,1):
            
            row = (i - 1) // 3 + 1
            colum = (i - 1) % 3
            
            if  i == 0:
                row = 4
                colum = 1

            Buttons.Create_button(i,row,colum,button_size = 24)
            
        #creates all operand buttons   
        Operands = ("x","/","+","-",)    
        row = 1
        for value in Operands:
            Buttons.Create_button(value,row, 3, button_size = 24)
            row += 1
        
        




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




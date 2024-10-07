import tkinter as tk
import json

Calc_Width = 250
Calc_Height = 500

            
            



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
            
        #Creates = button
            Buttons.Create_button("=",4,2,24)
        #Creates . (decimal) button
            Buttons.Create_button(".",4,0,24)
        #Creates delete button 
            Buttons.Create_button("delete",5,0,24,4,10)
            
    
        
        
class Calc_Buttons(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()  
        
    def Create_button(self,Button_Name,row=0,colum=0,button_size=2,colum_span=1,width=2):
        # Creates a button
        self.button = tk.Button(self, text=Button_Name, command= lambda name=Button_Name: self.button_clicked(name),font=("Helvetica", button_size),width=width)
        self.button.grid(row=row,column=colum,columnspan=colum_span)
        
    #updates jason with numbers and operators for current calculation
    def Update_Current_Calc_Json(self,AddCalc = 0,Delete = False):
        
        with open('Calculator/CalcData.json','r') as f:
            Calc_data = json.load(f)
        
        if Delete == False:
            print("updated json")
            
            
            Calc_data['Current Calculation'].append(AddCalc)
            
            with open('Calculator/CalcData.json', 'w') as f:
                json.dump(Calc_data, f, indent=4)
        elif Delete == True:
            deleted_calc = Calc_data['Current Calculation'].pop()
            
            with open('Calculator/CalcData.json', 'w') as f:
                json.dump(Calc_data, f, indent=4)
                print(f"Deleted: {deleted_calc}")
                
            
        

    def Update_inputfield(self,name):
        print("updated feild with:"+ str(name))
        
    
    def button_clicked(self,name):
        print(name)
        if name in [0,1,2,3,4,5,6,7,8,9]:
            self.Update_inputfield(name)
            print("number")
            self.Update_Current_Calc_Json(str(name))
            
        elif name in ["x","/","+","-",]:
            self.Update_inputfield(name)
            print("operand")
            self.Update_Current_Calc_Json(str(name))
        elif name == ".":
            self.Update_inputfield(name)
            print("decimal")
            self.Update_Current_Calc_Json(str(name))
        elif name == "delete":
            print("delete")
            self.Update_Current_Calc_Json(0,True)
        elif name == "=":
            print("run clac")
        else:
            print("Calc Error Button not in Registry check button clicked def in Calc buttons class")
            
            
            




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




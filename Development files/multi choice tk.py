import customtkinter


class page(): 
    def __init__(self):
         self.app = customtkinter.CTk() #creating the app 
         self.frame = customtkinter.CTkFrame(self.app)
         self.app.geometry("500x500") 
         customtkinter.set_appearance_mode('dark') #setting appreance mode, light/dark
         customtkinter.set_default_color_theme('blue') #theme of app/buttons

         self.frame.pack(pady=20, padx=60, fill='both', expand=True)

         self.textbox = customtkinter.CTkTextbox(master=self, width=200, corner_radius=0)
         self.textbox.insert('0.0', 'example text')

         self.buttonA = customtkinter.CTkButton(master=self.frame, text='A', command=self.button_print_answerA) 
         self.buttonB = customtkinter.CTkButton(master=self.frame, text='B', command=self.button_print_answerB) 
         self.buttonC = customtkinter.CTkButton(master=self.frame, text='C', command=self.button_print_answerC) 
         self.buttonD = customtkinter.CTkButton(master=self.frame, text='D', command=self.button_print_answerD) 


         for i in range (8):
              self.frame.grid_columnconfigure(i, weight=3,) # setting grid, columns 
         for i in range (8):
                   self.frame.grid_rowconfigure(i, weight=1,) # rows
        
         self.buttonA.grid(row=4, column=0, padx=1, pady=1) # button on the grid
         self.buttonB.grid(row=4, column=8, padx=1, pady=1)
         self.buttonC.grid(row=8, column=0, padx=1, pady=1)
         self.buttonD.grid(row=8, column=8, padx=1, pady=1)
         self.textbox.grid(row=0, column=4, sticky='nsew')

    def button_print_answerA(self):
        print('option a')
    def button_print_answerB(self):
          print('option b')
    def button_print_answerC(self):
          print('option c')
    def button_print_answerD(self):
          print('option d')

    



    def run(self):
          self.app.mainloop()

   



Running = page()
Running.run() #runs the app 
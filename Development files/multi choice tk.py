import customtkinter


class page(): 
    def __init__(self):
         self.app = customtkinter.CTk() #creating the app 
         self.frame = customtkinter.CTkFrame(self.app)
         self.app.geometry("500x500") 
         customtkinter.set_appearance_mode('dark') #setting appreance mode, light/dark
         customtkinter.set_default_color_theme('blue') 

         self.frame.pack(pady=20, padx=60, fill='both', expand=True)

         self.button = customtkinter.CTkButton(master=self.frame, text='A', command=self.button_print_answer) 
         

         for i in range (7):
              self.frame.grid_columnconfigure(i, weight=3,) # setting grid, columns 
         for i in range (7):
                   self.frame.grid_rowconfigure(i, weight=1,) # rows
        
         self.button.grid(row=1, column=4, padx=1, pady=1) 



    def button_print_answer(self):
        print('option a')

    



    def run(self):
          self.app.mainloop()

   



Running = page()
Running.run() 
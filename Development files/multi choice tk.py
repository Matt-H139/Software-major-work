import customtkinter


class page():
    def __init__(self):
         self.app = customtkinter.CTk("Mutiple Choice Quiz") #creating the app 
         self.frame = customtkinter.CTkFrame(self.app)
         self.app.geometry("400x400") 
         customtkinter.set_appearance_mode('light')
         customtkinter.set_default_color_theme('dark green') 

         self.frame.pack(pady=20, padx=60, fill='both', expand=True)


         for i in range (12):
              self.frame.grid_columnconfigure
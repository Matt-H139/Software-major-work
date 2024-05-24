import customtkinter

class Page(customtkinter.CTk):  # Inherit from customtkinter.CTk
    def __init__(self):
        super().__init__()  # Initialize the superclass
        
        self.geometry("500x500")
        customtkinter.set_appearance_mode("dark")  # Setting appearance mode
        customtkinter.set_default_color_theme("blue")  # Setting theme
        
        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        self.label = customtkinter.CTkLabel(master=self.frame, text='Quiz Title', fg_color='transparent') #setting label dimensions
        self.label.grid(row=0, column=4, sticky='nsew') #label in grid
        
        self.buttonA = customtkinter.CTkButton(master=self.frame, text='A', command=self.button_print_answerA) #button commands + labels
        self.buttonB = customtkinter.CTkButton(master=self.frame, text='B', command=self.button_print_answerB)
        self.buttonC = customtkinter.CTkButton(master=self.frame, text='C', command=self.button_print_answerC)
        self.buttonD = customtkinter.CTkButton(master=self.frame, text='D', command=self.button_print_answerD)
        
        for i in range(8):
            self.frame.grid_columnconfigure(i, weight=3)
            self.frame.grid_rowconfigure(i, weight=1)
        
        self.buttonA.grid(row=4, column=0, padx=1, pady=1) #setting buttons in grid
        self.buttonB.grid(row=4, column=8, padx=1, pady=1)
        self.buttonC.grid(row=8, column=0, padx=1, pady=1)
        self.buttonD.grid(row=8, column=8, padx=1, pady=1)

    def button_print_answerA(self):   # button commands 
        print('option a')
    
    def button_print_answerB(self):
        print('option b')
    
    def button_print_answerC(self):
        print('option c')
    
    def button_print_answerD(self):
        print('option d')

def run():
    app = Page()
    app.mainloop()

if __name__ == "__main__":
    run()

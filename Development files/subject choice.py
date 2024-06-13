from typing import Optional, Tuple, Union
import customtkinter 

class Page(customtkinter.CTk): 
    def __init__(self):
        super().__init__()

        self.geometry('500x500')
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme('blue')

        self.frame2 = customtkinter.CTkFrame(self)
        self.frame2.pack(pady =10, padx =10, fill='both', expand=True)

        self.Label2 = customtkinter.CTkLabel(master=self.frame2, text='Select Quiz Topic', fg_color='transparent')
        self.Label2.grid(row=0, column=3, sticky='nsew')

        self.options_buttons = []
        for i in range(4):
            Button1 = customtkinter.CTkButton(master=self.frame2, text='', command=lambda i=i: self.check_answer(i))
            self.options_buttons.append(Button1) 
            Button1.grid(row=i + 1, column=1, pady=5, padx=5)

        for i in range(10):
            self.frame.grid_columnconfigure(i, weight=3)
            self.frame.grid_rowconfigure(i, weight=1)


        self.questions = [
            {
                'question': 'Select Quiz Topic',
                'options': ['physics', 'biology', 'mathematics', 'italian'], 
                'correct': 0
            }
        ]
        

        self.current_question_index = 0 
        self.load_question()

    def load_question(self):
        question_data = self.questions[self.current_question_index]
        options = question_data['options']
        for i, option in enumerate(options):
            self.options_buttons[i].configure(text=option)

    


def run():
    app = Page()
    app.mainloop()

if __name__ == "__main__":
    run() 

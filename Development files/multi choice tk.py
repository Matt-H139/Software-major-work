import customtkinter
from get_questions import import_quiz_data

quiz_data = import_quiz_data()


class Page(customtkinter.CTk):  # Inherit from customtkinter.CTk
    def __init__(self):
        super().__init__()  # Initialize the superclass
        
        self.geometry("750x750") # Window size
        customtkinter.set_appearance_mode("dark")  # Setting appearance mode
        customtkinter.set_default_color_theme("blue")  # Setting theme
        
        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        self.feedback_label = customtkinter.CTkLabel(master=self.frame, text='Quiz Title', fg_color='transparent') #setting label dimensions + label name/title
        self.feedback_label.grid(row=0, column=4, sticky='nsew') #label in grid
        
        self.option_buttons = []
        for i in range(4):
            buttonA = customtkinter.CTkButton(master=self.frame, text='A', command=lambda i=i: self.check_answer(i)) #button commands + labels
            self.option_buttons.append(buttonA)    
            buttonA.grid(row=i + 1, column=4, padx=10, pady=10)    #setting buttons in grid
       
        for i in range(9):
            self.frame.grid_columnconfigure(i, weight=3)
            self.frame.grid_rowconfigure(i, weight=1)
        

        # self.questions = quiz_data
        self.questions = [

            quiz_data[0],
            quiz_data[1],
            quiz_data[2],
            quiz_data[3],
            quiz_data[4],
            quiz_data[5],
            quiz_data[6],
            quiz_data[7],
            quiz_data[8],
            quiz_data[9],
            quiz_data[10],
            quiz_data[11],
            quiz_data[12],
            quiz_data[13],
            quiz_data[14],
            quiz_data[15],
            quiz_data[16],
            quiz_data[17],
            quiz_data[18],
            quiz_data[19],
        ]

        self.current_question_index = 0
        self.load_question()

    def load_question(self):
        question_data = self.questions[self.current_question_index]
        self.feedback_label.configure(text=question_data["question"])

        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].configure(text=option)

    def check_answer(self, selected_option_index):
        correct_option_index = self.questions[self.current_question_index]["correct"]

        if selected_option_index == correct_option_index:
            self.feedback_label.configure(text="Correct!", text_color="green")
        else:
            self.feedback_label.configure(text="Incorrect!", text_color="red")

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.load_question()
        else:
            self.feedback_label.configure(text="Quiz Completed!")
            for button in self.option_buttons:
                button.configure(state='disabled')
            self.feedback_label.configure(text='')

def run():
    app = Page()
    app.mainloop()

if __name__ == "__main__":
    run()


# take the questions imported from quiz data 
# feed them into self.questions in interface
# test that a question appears
# think about 

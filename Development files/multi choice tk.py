import customtkinter
import csv 

def import_quiz_data():
    quiz_data = []
    with open('questions.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            options = [row['option_a'], row['option_b'], row['option_c'], row['option_d']]
            correct_answer = row['answer']
            quiz_data.append({
                'subject': row['subject'],
                'question': row['question'],
                'options': options,
                'correct_answer': correct_answer
            })
    return quiz_data

global quiz_data
quiz_data = import_quiz_data()

global score
score = 0 

unique_subjects = list(set(question['subject'] for question in quiz_data))

class Page(customtkinter.CTk):  # Inherit from customtkinter.CTk 
    def __init__(self, subject):
        super().__init__()  # Initialize the superclass
        
        self.geometry('500x500')
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme('blue')

        self.subject_frame = customtkinter.CTkFrame(self)
        self.subject_frame.pack(pady =10, padx =10, fill='both', expand=True)

        self.Label2 = customtkinter.CTkLabel(master=self.subject_frame, text='Select Quiz Topic', fg_color='transparent')
        self.Label2.grid(row=0, column=5, sticky='nsew')

        self.options_buttons2 = []
        for i, option in enumerate(subject): 
            Button = customtkinter.CTkButton(master=self.subject_frame, text=option, command=lambda opt=option: self.open_frame(opt))
            self.options_buttons2.append(Button) 
            Button.grid(row=i + 1, column=5, pady=5, padx=5)

        for i in range(10):
            self.subject_frame.grid_columnconfigure(i, weight=3)
            self.subject_frame.grid_rowconfigure(i, weight=1)


        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack_forget()

        self.questions = quiz_data
        self.current_question_index = 0

        self.retry_button = customtkinter.CTkButton(master=self.frame, text='Retry Or Select New Topic', command=self.reset_quiz)

    def open_frame(self, option): 

        # get questions based on chosen option
        filtered_questions = [q for q in quiz_data if q['subject'] == option]

        print(f"Selected option: {option}")
        self.subject_frame.pack_forget()
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text=f"{option} Quiz", fg_color="transparent")
        self.label.grid(row=0, column=3, columnspan=3, sticky="news") 

        self.feedback_label = customtkinter.CTkLabel(master=self.frame, text='Quiz Title', fg_color='transparent') #setting label dimensions + label name/title
        self.feedback_label.grid(row=1, column=4, sticky='nsew') #label in grid
        
        self.option_buttons = []

        for i in range(4):
            buttonA = customtkinter.CTkButton(master=self.frame, text='A', command=lambda i=i: self.check_answer(i)) #button commands + labels
            self.option_buttons.append(buttonA)    
            buttonA.grid(row=i + 2, column=4, padx=10, pady=10)    #setting buttons in grid
       
        for i in range(9):
            self.frame.grid_columnconfigure(i, weight=3)
            self.frame.grid_rowconfigure(i, weight=1)
        

        self.questions = filtered_questions
        self.current_question_index = 0
        self.load_question()

    def load_question(self):
        question_data = self.questions[self.current_question_index]
        self.feedback_label.configure(text=question_data["question"])

        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].configure(text=option)

    def check_answer(self, selected_option_index):
        question_data = self.questions[self.current_question_index]
        correct_option_index = ord(question_data['correct_answer']) - ord('a')  # Convert 'a', 'b', 'c', 'd' to 0, 1, 2, 3

        global score
        if selected_option_index == correct_option_index:
            score += 1 

        self.current_question_index += 1

        if self.current_question_index < len(self.questions): 
            self.load_question()
        else:
            for button in self.option_buttons:
                button.configure(state='disabled')
            self.feedback_label.configure(text=f"Quiz Completed!\n Your score: {score} ")  # Displays Text in a label once all questions have been answered
            print(score)
            
            self.retry_button.grid(row=7, column=4, pady=10, padx=10)

    def reset_quiz(self):
        global score
        score = 0
        self.retry_button.pack_forget()
        self.frame.pack_forget()
        self.subject_frame.pack(pady=10, padx=10, fill='both', expand=True)

def run():
    app = Page(unique_subjects)
    app.mainloop()

if __name__ == "__main__":
    run() 

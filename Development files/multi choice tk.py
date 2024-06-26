import customtkinter
import csv 

def import_quiz_data(): # import data from csv
    quiz_data = []
    with open('questions.csv', 'r') as file:
        reader = csv.DictReader(file) # reads csv file
        for row in reader:
            options = [row['option_a'], row['option_b'], row['option_c'], row['option_d']] 
            correct_answer = row['answer'] # the correct answer is recognised by the string in answer column & the letter option selected match (option_a, b, c, d)
            quiz_data.append({
                'subject': row['subject'],
                'question': row['question'],
                'options': options,
                'correct_answer': correct_answer
            })
    return quiz_data

global quiz_data
quiz_data = import_quiz_data() # importing the data from csv file through get_questions 

global score # global variable, score starts at 0
score = 0 

unique_subjects = list(set(question['subject'] for question in quiz_data)) #filters questions through the subjects column in csv file

class Page(customtkinter.CTk):  # Inherit from customtkinter.CTk 
    def __init__(self, subject):
        super().__init__()  # Initialize the superclass
        
        self.geometry('500x500') # dimensions of frame
        customtkinter.set_appearance_mode("dark") # background/primary colour 
        customtkinter.set_default_color_theme('blue') # colour theme/secondary colour 

        self.subject_frame = customtkinter.CTkFrame(self) # initialising the subject selection frame
        self.subject_frame.pack(pady =10, padx =10, fill='both', expand=True)

        self.Label2 = customtkinter.CTkLabel(master=self.subject_frame, text='Select Quiz Topic', fg_color='transparent') # label within the subject frame 
        self.Label2.grid(row=0, column=5, sticky='nsew') # label in grid, place in the frame

        self.options_buttons2 = [] # subject selection buttons
        for i, option in enumerate(subject): 
            Button = customtkinter.CTkButton(master=self.subject_frame, text=option, command=lambda opt=option: self.open_frame(opt)) # initialising button. command lambda = used for defining an anonymous function
            self.options_buttons2.append(Button) # can add more buttons if necessary 
            Button.grid(row=i + 1, column=5, pady=5, padx=5) # place of buttons in the frame, buttons in the grid

        for i in range(10):
            self.subject_frame.grid_columnconfigure(i, weight=3) 
            self.subject_frame.grid_rowconfigure(i, weight=1)


        self.frame = customtkinter.CTkFrame(self) #new frame for quiz 
        self.frame.pack_forget()  # hide the frame until called 

        self.questions = quiz_data # questions are taken from quiz_data/ csv file
        self.current_question_index = 0 # the quiz start at the first question. The index of questions starts at 0

        self.retry_button = customtkinter.CTkButton(master=self.frame, text='Retry Or Select New Topic', command=self.reset_quiz) # initialising return button

    def open_frame(self, option): # open quiz frame when subject is selected 

        # get questions based on chosen option
        filtered_questions = [q for q in quiz_data if q['subject'] == option] # use the questions associated with the same subject 

        print(f"Selected option: {option}") # print the selected subject
        self.subject_frame.pack_forget() # hide the subject frame 
        self.frame.pack(pady=20, padx=20, fill="both", expand=True) 

        self.label = customtkinter.CTkLabel(master=self.frame, text=f"{option} Quiz", fg_color="transparent") # displaying what quiz the user is doing, eg. 'Physics quiz'
        self.label.grid(row=0, column=3, columnspan=3, sticky="news") # setting label in the grid 

        self.feedback_label = customtkinter.CTkLabel(master=self.frame, text='Quiz Title', fg_color='transparent') #setting label dimensions + label name/title
        self.feedback_label.grid(row=1, column=4, sticky='nsew') #label in grid
        
        self.option_buttons = [] 

        for i in range(4):
            buttonA = customtkinter.CTkButton(master=self.frame, text='A', command=lambda i=i: self.check_answer(i)) #button commands + text in button
            self.option_buttons.append(buttonA)    
            buttonA.grid(row=i + 2, column=4, padx=10, pady=10)    #setting buttons in grid
       
        for i in range(9):
            self.frame.grid_columnconfigure(i, weight=3) # setting grid of frame
            self.frame.grid_rowconfigure(i, weight=1)
        

        self.questions = filtered_questions
        self.current_question_index = 0
        self.load_question()

    def load_question(self): # loads in questions when quiz frame is called 
        question_data = self.questions[self.current_question_index]
        self.feedback_label.configure(text=question_data["question"]) # quiz questions use quiz data from csv file from questions column 

        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].configure(text=option)  # buttons use quiz data from csv file in the option_a, b, c, d columns

    def check_answer(self, selected_option_index):
        question_data = self.questions[self.current_question_index]
        correct_option_index = ord(question_data['correct_answer']) - ord('a')  # Convert 'a', 'b', 'c', 'd' to 0, 1, 2, 3. string to integer

        global score
        if selected_option_index == correct_option_index: # if the selected option = correct option add +1 to score
            score += 1 

        self.current_question_index += 1 # score is increased by +1 on each correct answer

        if self.current_question_index < len(self.questions): # if there are still unanswered quesions remaining, load them
            self.load_question()                        
        else:                                                 # otherwise display that the quiz is completed and the user's score
            for button in self.option_buttons:
                button.configure(state='disabled')
            self.feedback_label.configure(text=f"Quiz Completed!\n Your score: {score} ")  # Displays Text in a label once all questions have been answered
            print(score)
            
            self.retry_button.grid(row=7, column=4, pady=10, padx=10) # place of retry button in the frame

    def reset_quiz(self): # if retry button is clicked hides the retry button and quiz frame 
        global score # resets user's score when retry button is clicked 
        score = 0
        self.retry_button.pack_forget()
        self.frame.pack_forget()
        self.subject_frame.pack(pady=10, padx=10, fill='both', expand=True) # then returns back to the subject selection frame

def run():      # runs app
    app = Page(unique_subjects)
    app.mainloop()

if __name__ == "__main__":
    run() 

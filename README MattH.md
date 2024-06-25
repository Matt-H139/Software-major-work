# CustomTkinter Quiz Application, 'Custom Quizzer'

## Description
This project is a quiz application built using `customtkinter` that dynamically loads questions from a CSV file and presents them to the user based on the selected topic. The user's score is tracked and displayed at the end of the quiz.

## Installation Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Matt-H139/Software-major-work/tree/master
   cd Software-major-work/

2. **Install Python packages**
   pip install customtkinter
   pip install pandas

## How To Use
1. **Run The Application**
   multi choice tk.py (Also have get_questions.py & questions.csv open when running application)
2. Select a quiz topic from the initial menu
3. Answet the questions by clicking on appropriate buttons
4. View your score at the end of the quiz
5. Add your own set of questions to questions.csv and redo the quiz with your own set of custom questions

## Acknowledgements
- Thanks to Customtkinter for the UI framework
- Thanks to Mr Fong, Mr Jeffery and Iggy M for their assistance and help in the development in the project

## Author Details
Name: Matthew K Hill
Contact: mhill@student.saintaug.nsw.edu.au
Github: Matt-H139

## Clean Directory Structure
── multi_choice_tk.py       # Main Python script
── questions.csv            # CSV file containing quiz questions
── get_questions.py         # pandas file which loads data from CSV file
── README MattH.md          # This README file 

## Documentation
For detailed documentation, please refer to: https://saintaugsydney-my.sharepoint.com/:w:/r/personal/mhill_student_saintaug_nsw_edu_au/Documents/Software%20Major%20Work%20Documentation%20Matthew%20Hill.docx?d=w989333ad3d1c40dfb793cbcd9790414d&csf=1&web=1&e=ySvLzZ

## Additional details
- Dependencies: Ensure you have customtkinter and pandas installed
- CSV Format: The questions.csv file should have the following columns: 'subject', 'question', 'options', 'answer'

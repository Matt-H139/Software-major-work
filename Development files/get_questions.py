import pandas as pd


# Load the data from the CSV file
df = pd.read_csv('questions.csv')

quiz_data = []
for index, row in df.iterrows():
    question_dict = {
        "subject": row["subject"],
        "question": row["question"] if pd.notna(row["question"]) else "No question provided",
        "options": [row["option_a"], row["option_b"], row["option_c"], row["option_d"]],
        "correct": row["answer"]
    }
    quiz_data.append(question_dict)

# Print the quiz data to verify
for question in quiz_data:
    if question["subject"] == "Physics":
        print(question)
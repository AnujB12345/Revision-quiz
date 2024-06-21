import tkinter as tk
import random
from questionbank import physics_quiz, maths_quiz, business_quiz

# Initialize global variables
score = 0
question_number = 1
current_quiz = []

# Function to start the quiz based on subject choice
def start_quiz():
    global current_quiz, score, question_number
    subject_choice = subject_var.get()
    if subject_choice in subjects:
        current_quiz = list(subjects[subject_choice])
        random.shuffle(current_quiz)
        score = 0
        question_number = 1
        display_question()
    else:
        subject_label.config(text="Invalid option, try again!")

# Function to display the current question
def display_question():
    if question_number <= 10:
        question = current_quiz[question_number - 1]["question"]
        question_label.config(text=f"Q{question_number}: {question}")
        question_label.pack(pady=10)
        answer_entry.pack(pady=10)
        submit_button.pack(pady=10)
    else:
        show_results()

# Function to submit the answer and move to the next question
def submit_answer():
    global score, question_number
    user_answer = answer_entry.get().lower().strip()
    correct_answer = current_quiz[question_number - 1]["answer"]
    if user_answer == correct_answer:
        score += 1

    question_number += 1
    answer_entry.delete(0, tk.END)
    display_question()

# Function to show the results at the end of the quiz
def show_results():
    question_label.pack_forget()
    answer_entry.pack_forget()
    submit_button.pack_forget()

    result_label.config(text=f"Out of 10 questions, you got {score} correct answers. Well Done!")
    result_label.pack(pady=10)
    play_again_button.pack(pady=10)

# Function to reset the game for another round
def play_again():
    result_label.pack_forget()
    play_again_button.pack_forget()
    subject_label.pack(pady=10)
    subject_menu.pack(pady=10)
    start_button.pack(pady=10)

# Set up the main window
root = tk.Tk()
root.title("A Level Revision Quiz")

# Initialize subjects
subjects = {"Physics": physics_quiz, "Maths": maths_quiz, "Business": business_quiz}

# Set up the initial widgets
subject_label = tk.Label(root, text="Choose a subject to be tested on (Physics, Maths, Business):", font=("Arial", 16))
subject_label.pack(pady=10)

subject_var = tk.StringVar()
subject_menu = tk.OptionMenu(root, subject_var, *subjects.keys())
subject_menu.pack(pady=10)

start_button = tk.Button(root, text="Start Quiz", command=start_quiz, font=("Arial", 16))
start_button.pack(pady=10)

question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=500)
answer_entry = tk.Entry(root, font=("Arial", 16))
submit_button = tk.Button(root, text="Submit Answer", command=submit_answer, font=("Arial", 16))

result_label = tk.Label(root, text="", font=("Arial", 16))
play_again_button = tk.Button(root, text="Play Again", command=play_again, font=("Arial", 16))

# Start the Tkinter event loop
root.mainloop()
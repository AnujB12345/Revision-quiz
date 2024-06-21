import time
import random
from questionbank import physics_quiz
from questionbank import maths_quiz
from questionbank import business_quiz

physics = list(physics_quiz) #converts the dictionary's keys into a list

score = 0
question_number = 1
print("This is an A level revision quiz, where we will give you 10 MCQs on a subject of your choice(physics, maths, business)")
time.sleep(1)

def choice():
   subjects = ["Physics","Maths","Business"]
   subject_choice = input("Choose a subject to be tested on(physics, maths, business): ").title()
   if subject_choice in subjects:
      if subject_choice == "Physics":
         physics_questions()
      elif subject_choice == "Maths":
         maths_questions()
      elif subject_choice == "Business":
         business_questions()
   else:
      print("Invalid option, try again!")
      choice()

def physics_questions():
   global score, question_number
   score= 0
   question_number = 1
   random.shuffle(physics_quiz)
   for item in physics_quiz:
      question = item["question"]
      correct_answer = item["answer"]
      user_answer = input(f"Q{question_number}: {question}").lower().strip()
      if user_answer == correct_answer:
         print("Well done, you are right!")
         score +=1
      else:
         print("Unfortunately, you got it wrong")
      question_number +=1
   results()

def maths_questions():
   global score, question_number
   score = 0
   question_number = 1
   random.shuffle(maths_quiz)
   for item in maths_quiz:
      question = item["question"]
      correct_answer = item["answer"]
      user_answer = input(f"Q:{question_number}: {question}").lower().strip()
      if user_answer == correct_answer:
         print("Well done, you are right!")
         score +=1
      else:
         print("Unfortunately, you got it wrong")
      question_number +=1
   results()

def business_questions():
   global score, question_number
   question_number = 1
   score = 0
   random.shuffle(business_quiz)
   for item in business_quiz:
      question = item["question"]
      correct_answer = item["answer"]
      user_answer = input(f"Q{question_number}:{question}").lower().strip()
      if user_answer == correct_answer:
         print("Well done, you are right!")
         score +=1
      else:
         print("Unfortunately, you got it wrong")
      question_number +=1
   results()

def results():
   global score
   result = input("Do you want to receive your results(type y)?: ").lower().strip()
   if result == "y":
      print(f"Out of 10 questions, you got {score} correct answers. Well Done!")
      play_again()
   else:
      play_again()

def play_again():
   again = input("Press any key to continue playing or 1 to quit")
   if again == "1":
      print("Goodbye!")
      exit()
   else:
      choice()

choice()
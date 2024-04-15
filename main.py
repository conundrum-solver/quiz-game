from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

my_quiz = QuizBrain(question_bank)
while my_quiz.still_has_question():
    my_quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {my_quiz.score}/{my_quiz.question_number}")

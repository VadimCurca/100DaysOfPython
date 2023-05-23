from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = [Question(question["question"], question["correct_answer"]) for question in question_data]

quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

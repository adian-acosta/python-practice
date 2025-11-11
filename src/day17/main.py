from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for i in range(len(question_data)):
    question = question_data[i]["question"]
    answer = question_data[i]["correct_answer"]
    obj = Question(question, answer)
    question_bank.append(obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("you've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
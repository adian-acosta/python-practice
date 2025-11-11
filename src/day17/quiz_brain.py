class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        choice = input(f"Q.{self.question_number + 1}: {question.text} (True/False)?: ")

        self.check_answer(choice, question.answer)

        self.question_number += 1

    def check_answer(self, choice, answer):
        if choice == answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That is inccorect")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number + 1}\n\n")

from question_model import Question


class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}. {current_question.text}? (True/False): ")
        self.check_answer(current_question.answer, user_answer)

    def check_answer(self, correct_answer, answer):
        if correct_answer.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score} / {self.question_number}")
        print("\n")

    def print_score(self):
        print(f"Your finale score was: {self.score} / {self.question_number}")
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

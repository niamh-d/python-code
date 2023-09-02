class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score= 0
        self.game_over = False

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (T/F)?: ").lower()
        correct_answer = question.answer
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        result = user_answer == correct_answer.lower()
        if result:
            print(f"Correct answer! The answer was '{correct_answer}'.")
            self.score += 1
            print(f"Your current score: {self.score}")
            if self.score == 12:
                print("Congrats! You reached the end of the quiz and scored maximum points!")
                self.game_over = True
        else:
            print(f"I'm sorry! That was the wrong answer! The answer was '{correct_answer}'.")
            print(f"Game over! Your final score: {self.score}")
            self.game_over = True



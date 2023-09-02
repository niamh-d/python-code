from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

quiz = QuizBrain(question_bank)

for _ in question_data:

    question = Question(_["text"], _["answer"])
    question_bank.append(question)

while not quiz.game_over:
    quiz.next_question()
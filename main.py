from question_model import Question, logo
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    q = Question(i["text"], i["answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()
    print()
    print()
print(f'\n\nYou have completed the quiz!\nYour final score was {quiz.score}/{quiz.len}')  #

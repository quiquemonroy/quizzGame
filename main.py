from question_model import Question, logo
from data import question_list
from quiz_brain import QuizBrain

question_bank = []
for i in question_list:
    q = Question(i["question"]["text"], i["correctAnswer"], i["incorrectAnswers"])
    question_bank.append(q)

# print(question_bank[0].responses)
quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()
    print()
    print()
print(f'\n\nYou have completed the quiz!\nYour final score was {quiz.score}/{quiz.len}')

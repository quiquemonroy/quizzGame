
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_have_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        num = self.question_number
        current = self.question_list[num]
        self.question_number += 1
        ans = input(f'Q{self.question_number}: {current.q}. (T)rue or (F)alse?').lower().strip()
        correct = current.a.lower().strip()
        self.check_answer(ans, correct)

    def check_answer(self, ans, correct):
        if ans == correct:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f'the correct answer was: {correct.capitalize()}')
        print(f'Your current score is {self.score}/{self.question_number}')

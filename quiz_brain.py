import random, time, os
from question_model import logo
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.len = len(self.question_list)
        self.asked = 0

    def still_have_questions(self):
        return self.asked < self.len

    def next_question(self):
        num = self.question_number
        current = random.choice(self.question_list)
        self.asked += 1
        print(logo)
        ans = input(f'Q{self.asked}: {current.q}. (T)rue or (F)alse?').lower().strip()
        correct = current.a.lower().strip()
        self.check_answer(ans, correct)
        self.question_list.remove(current)


    def check_answer(self, ans, correct):
        if ans[0] == correct[0]:
            self.score += 1
            print("\nYou got it right!")
            print(f'the correct answer was: {correct.capitalize()}')
            print(f'Your current score is {self.score}/{self.asked}')
            time.sleep(2)
            os.system("clear")
        elif ans == "q":
            print("\nThanks for playing.")
            print(f'the correct answer was: {correct.capitalize()}, btw')
            print(f'Your score is {self.score}/{self.asked}')
            self.asked += 600
        else:
            print("\nThat's wrong!")
            print(f'the correct answer was: {correct.capitalize()}')
            print(f'Your current score is {self.score}/{self.asked}')
            time.sleep(2)
            os.system("clear")

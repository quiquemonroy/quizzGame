import os
import random
import time

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
        current = random.choice(self.question_list)
        random.shuffle(current.responses)

        print(logo)
        print(f'Your score is: {self.score} out of {self.asked}')
        self.asked += 1
        question = f'Q{self.asked}: {current.q}'
        print(f'{question}\n')
        for i in range(0,len(current.responses)):
            print(f'   {i+1}: {current.responses[i]}')
        while True:
            try:
                ans = int(input("1,2, 3 or 4?   > ").lower().strip())
                break
            except:
                print("Please, type a number between 1 and 4. Type 9 for exit.")
                continue
        correct = current.a
        self.check_answer(ans, correct, current)
        self.question_list.remove(current)

    def check_answer(self, ans, correct,current):
        if ans == 0:
            print("\nThanks for playing.")
            print(f'the correct answer was: {correct.capitalize()}, btw')
            print(f'Your score is {self.score}/{self.asked-1}')
            self.asked += 600

        elif current.responses[ans-1] == correct:
            self.score += 1
            print("\nYou got it right!")
            print(f'the correct answer was: {correct.capitalize()}')
            print(f'Your current score is {self.score}/{self.asked}')
            time.sleep(2)
            os.system("clear")
        else:
            print("\nThat's wrong!")
            print(f'the correct answer was: {correct.capitalize()}')
            print(f'Your current score is {self.score}/{self.asked}')
            time.sleep(2)
            os.system("clear")

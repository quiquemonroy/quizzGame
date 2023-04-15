
class NewQuestions:
    def __init__(self):
        self.output = []

    def generate_new_questions(self,data):
        for i in data["results"]:
            d = {"text" :i["question"],"answer": i["correct_answer"]}
            self.output.append(d)

        # question = dict[i]["question"]
        # ans = dict[i][0]["correct_answer"]
        # question_data.append({"text":question,"answer":ans})



class NewQuestions:
    def __init__(self,data):
        self.data = data
        self.output = []
    def generate_new_questions(self):
        for i in self.data["results"]:
            d = {"text" :i["question"],"answer": i["correct_answer"]}
            self.output.append(d)

        # question = dict[i]["question"]
        # ans = dict[i][0]["correct_answer"]
        # question_data.append({"text":question,"answer":ans})


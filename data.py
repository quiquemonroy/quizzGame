import json,requests,time

false = False
true = True

# new = NewQuestions()


# question_data = new.output
# print(len(new.output))




data= requests.get("https://the-trivia-api.com/v2/questions?limit=50")
question_list = data.json()


# print(json.dumps(preguntas, indent = 2))
data2= requests.get("https://the-trivia-api.com/v2/questions?limit=50")
b = data2.json()
for i in b:
    question_list.append(i)
# time.sleep(2)
data3= requests.get("https://the-trivia-api.com/v2/questions?limit=50")
c = data2.json()
for i in c:
    question_list.append(i)

print(len(question_list))



# question_list = [
#   {
#     "category": "geography",
#     "id": "623386e20161109f922aabec",
#     "correctAnswer": "Washington D.C.\u00a0",
#     "incorrectAnswers": [
#       "Budapest",
#       "Freetown",
#       "New Delhi"
#     ],
#     "question": {
#       "text": "Which capital city stands on the Potomac River?"
#     },
#     "tags": [
#       "geography"
#     ],
#     "type": "text_choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": false
#   },
#   {
#     "category": "film_and_tv",
#     "id": "622a1c347cc59eab6f94fa7e",
#     "correctAnswer": "Jack Nicholson",
#     "incorrectAnswers": [
#       "Charles Durning",
#       "John Lithgow",
#       "Sam Shepard"
#     ],
#     "question": {
#       "text": "Who won the 1983 Academy Award for Best Supporting Actor for playing the role of Garrett Breedlove in Terms of Endearment?"
#     },
#     "tags": [
#       "academy_awards",
#       "film",
#       "acting",
#       "film_and_tv"
#     ],
#     "type": "text_choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": false
#   }
# ]
# question_list = []
# for i in question_list_raw:
#   dict = {}
#   dict["question"]=i["question"]["text"]
#   dict["correctAnswer"] = i["correctAnswer"]
#   dict["incorrectAnswers"] = i["incorrectAnswers"]
#   question_list.append(dict)
# print(question_list)
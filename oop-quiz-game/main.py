from data import  question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    ques_text = question['text']
    ques_answer = question['answer']
    new_question = Question(ques_text, ques_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("****************The quiz has finished!****************")
print(f"****************Your final score is : {quiz.score}/{quiz.question_number}****************")

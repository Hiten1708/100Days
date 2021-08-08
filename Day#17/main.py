from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []


for text in question_data:
  question = text["text"]
  answer = text["answer"]
  question_bank.append(Question(question, answer))


quiz = QuizBrain(question_bank)


while quiz.still_has_question():
  quiz.next_question()
  quiz.still_has_question()



print(f"GameOver, Thanks for playing. Your overall score is {quiz.score}/{len(question_bank)}")
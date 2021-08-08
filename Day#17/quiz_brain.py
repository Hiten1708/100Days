class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 0
    self.question_list = q_list
    self.score = 0
  
  def still_has_question(self):
    if (self.question_number) < len(self.question_list):
      return True
    else:
      return False

  def next_question(self):
    choice = input(f"Q.{self.question_number + 1} {self.question_list[self.question_number - 1].text} (True/False)")
    self.question_number += 1
    answer = self.question_list[self.question_number - 1].answer
    self.check_answer(choice, answer)
  
  def check_answer(self, wrote, right):
    if wrote.lower() == right.lower():
      print("you got it right!")
      self.score += 1
    else:
      print("You were wrong")
    print(f"the correct answer was {right}")
    print(f"your current score is {self.question_number}/{self.score}")
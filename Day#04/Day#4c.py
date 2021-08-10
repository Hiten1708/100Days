import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
RPS = ['r', 'p', 's']

auto_choice = random.choice(RPS)

choice = input("Hey! Welcome to rock paper and scissor game... type 'r' for rock, 's' for scissor ,and 'p' for paper\n").lower()

if auto_choice == choice:
  print("It's Draw, Try again")
elif auto_choice == "r" and choice == "s":
  print("Computer:\n" + rock)
  print("Player:\n" + scissors)
  print("Computer Wins")
elif auto_choice == "p" and choice == "s":
  print("Computer:\n" + paper)
  print("Player:\n" + scissors)
  print("Player Wins")
elif auto_choice == "p" and choice == "r":
  print("Computer:\n" + paper)
  print("Player:\n" + rock)
  print("Computer Wins")
elif auto_choice == "s" and choice == "r":
  print("Computer:\n" + scissors )
  print("Player:\n" + rock)
  print("Player Wins")
elif auto_choice == "r" and choice == "p":
  print("Computer:\n" + rock)
  print("Player:\n" + paper)
  print("Player Wins")
elif auto_choice == "s" and choice == "p":
  print("Computer:\n" + scissors)
  print("Player:\n" + paper)
  print("Computer Wins")
else:
  print("Enter a valid variable")

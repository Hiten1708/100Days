#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

NUMBER = int(random.randint(0, 100))
print(f"Welcome to the guessing game,\n {logo}")
difficulty = input("Choose the difficulty: Enter 'easy' or 'hard'\n").lower()
if difficulty == "easy":
  attempts_limit = 10
  print(f"You have chosen '{difficulty.capitalize()}' difficulty, so you have {attempts_limit} attempts")
elif difficulty == "hard":
  attempts_limit = 5
  print(f"You have chosen '{difficulty.capitalize()}' difficulty, so you have {attempts_limit} attempts")

attempts = 0
gameover = False

while attempts < attempts_limit and not gameover:
  guess = int(input("Make a guess: "))
  if guess > NUMBER:
    attempts += 1
    print(f"Too high, guess again \n Attempts: {attempts}")
  elif guess < NUMBER: 
    attempts += 1
    print(f"Too low, guess again\n Attempts: {attempts}")
  elif guess == NUMBER:
    attempts += 1
    print("You guessed it right, Thank you for playing.\n Good Bye")
    gameover = True

if not gameover:
  print("You didn't guessed it right, You lost")
elif attempts < attempts_limit:
  print("You ran out of attempts, You lost")


from replit import clear 
from art import logo
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
resume = input('Enter "yes" to enter the game, else enter "e" to exit\n').lower()

while resume == "yes": 
  player_cards = [random.choice(deck), random.choice(deck)]
  computer_cards = [random.choice(deck), random.choice(deck)]

  while (player_cards[0] + player_cards[1]) > 21 and (computer_cards[0] + computer_cards[1]) > 21:
    player_cards = [random.choice(deck), random.choice(deck)]
    computer_cards = [random.choice(deck), random.choice(deck)]
  
  def game():
    clear()
    print(logo)
    cont = "y" 
    total1 = 0
    total2 = 0
    for card1 in player_cards:
      total1 += card1
    for card2 in computer_cards:
      total2 += card2

    for n, i in enumerate(player_cards):
      if i == 11 and total1 > 21:
        player_cards[n] = 1
    for n, i in enumerate(computer_cards):
      if i == 11 and total2 > 21:
        computer_cards[n] = 1

    total1 = 0
    total2 = 0
    for card1 in player_cards:
      total1 += card1
    for card2 in computer_cards:
      total2 += card2
    
    
    while total2 < 17:
      computer_cards.append(random.choice(deck))
      for card2 in computer_cards:
        total2 += card2
    
    while cont == "y" and total1 < 21:
      total1 = 0
      total2 = 0
      for card1 in player_cards:
        total1 += card1
      for card2 in computer_cards:
        total2 += card2
      print(f"your cards are {player_cards} and your score is {total1}\n")
      print(f"One of the computer cards is {computer_cards[0]}\n")
      cont = input("if you want to draw a second card then enter 'y' or to pass enter 'n'\n").lower()
      if cont == "y":
        player_cards.append(random.choice(deck))
        total1 = 0
        total2 = 0
        for card1 in player_cards:
          total1 += card1
        for card2 in computer_cards:
          total2 += card2
        for n, i in enumerate(player_cards):
          if i == 11 and total1 > 21:
            player_cards[n] = 1
        for n, i in enumerate(computer_cards):
          if i == 11 and total2 > 21:
            computer_cards[n] = 1
        total1 = 0
        total2 = 0
        for card1 in player_cards:
          total1 += card1
        for card2 in computer_cards:
          total2 += card2
      else:
        cont = "n"
    
    if total1 > total2:
      if total1 == 21:
        return f"You win by Blackjack\n Your Score: {player_cards}\n Computer Score:{computer_cards}"
      elif total1 > 21:
        return f"Computer wins because you are busted\n Your Score: {player_cards}\n Computer Score:{computer_cards}"
      else:
        return f"Computer lost, You win\n Your Score: {player_cards}\n Computer Score:{computer_cards}"
    elif total1 < total2:
      if total2 == 21:
        return f"Computer wins by Blackjack\n Your Score: {player_cards}\n Computer Score:{computer_cards}"
      elif total2 > 21:
        return f"You win because, Computer is busted\n Your Score: {player_cards}\n Computer Score:{computer_cards}"
      else:
        return f"Computer wins, you lost\n Your Score: {player_cards}\n Computer Score:{computer_cards}"
    else:
       return f"It's Draw\n Your Score: {player_cards}\n Computer Score:{computer_cards}"

  game()
  print(game())

  resume = input('do you want to play a new game? or exit the game? To resume enter "yes" or to exit enter "e"\n').lower()




############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


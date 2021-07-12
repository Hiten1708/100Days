import random

ht = ["heads", "tails"]

choice = input("Choose 'Heads' or 'tails'").lower()

if choice == random.choice(ht):
	print("You Win")
else:
	print("you lose")

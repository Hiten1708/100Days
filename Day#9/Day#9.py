from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

bidding= []
def name_adder(nom, baji):
    bidders = {}
    bidders["Name"] = nom
    bidders["Bid"] = baji
    bidding.append(bidders)
resume = "yes"
while resume == "yes":
  clear()
  print(logo)
  print("Welcome to this bidding")
  Name = input("Enter the bidder's name:\n")
  Bid = int(input("Enter the amount you wanna bid \n$"))
  name_adder(nom = Name, baji = Bid)
  resume = input("Are there any more bidders? Enter 'yes' to continue or 'no' to stop\n").lower()
highest_bid = 0
highest_bidder = ''
for name in bidding:
  if name["Bid"] > highest_bid:
    highest_bid = name["Bid"]
    highest_bidder = name["Name"]

print(f"Winner of this bidding is {highest_bidder} with a bid of ${highest_bid}")
from art import logo
from game_data import data
from art import vs
import random
from replit import clear


def comparison(list1, list2):
  if list1["follower_count"] > list2["follower_count"]:
    return "a"
  elif list1["follower_count"] < list2["follower_count"]:
    return "b"
  else:
    return "same"

def higher(list1, list2):
  if list1["follower_count"] > list2["follower_count"]:
    return list1
  elif list1["follower_count"] < list2["follower_count"]:
    return list2
  else:
    return list1

point = 0
clear()
print(f"{logo}\nWelcome to higher or lower game." )
gameover = False

alist = random.choice(data)
blist = random.choice(data)

while not gameover:
  aname = alist["name"]
  aprofession = alist["description"]
  acountry = alist["country"]
  afollowers = alist["follower_count"]
  
  bname = blist["name"]
  bprofession = blist["description"]
  bcountry = blist["country"]
  bfollowers = blist["follower_count"]

  print(f"{aname}, a {aprofession}, from {acountry}")
  print(vs)
  print(f"{bname}, a {bprofession}, from {bcountry}")
  print(f"points:{point}")

  choice = input("Which one do you think has more number of followers in instagram? Enter 'A' or 'B' or 'Same'\n").lower()
    
  answer = comparison(alist, blist)
  winner = higher(alist, blist)

  if answer == choice:
    alist = winner
    blist = random.choice(data)
    point += 1
  else:
    gameover = True


print(f"GameOver, you earned {point} points")


  

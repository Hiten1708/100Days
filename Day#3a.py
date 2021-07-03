name1 = input("What is your name? \n")
name2 = input("What is your partner's name? \n")

n1 = name1.lower()
n2 = name2.lower()

n1t = n1.count("t")
n2t = n2.count("t")

n1r = n1.count("r")
n2r = n2.count("r")

n1u = n1.count("u")
n2u = n2.count("u")

n1e = n1.count("e")
n2e = n2.count("e")

n1l = n1.count("l")
n2l = n2.count("l")

n1o = n1.count("o")
n2o = n2.count("o")

n1v = n1.count("v")
n2v = n2.count("v")

n1e = n1.count("e")
n2e = n2.count("e")

fd = n1t + n1r + n1u + n1e + n2t + n2u + n2r + n2e
sd = n1l + n1o + n1v + n1e + n2l + n2o + n2v + n2e

score = 10*fd + sd

if score >= 90 or score <= 10:
  print("Your relationship is like coke and mentos")
if score <= 50 and score >= 40:
  print("Your relationship is alright") 
else:
  print(score)
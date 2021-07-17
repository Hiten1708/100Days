from art import logo
from replit import clear

def operation(num1, num2, operator):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 + num2
  elif operator == "/":
    return num1/num2
  elif operator == "*":
    return num1*num2
  else:
    return "You have entered invalid operator!"


resume = 'new'

while resume == "new":
  clear()
  print(logo)
  
  n1 = int(input("Whats your first number? \n"))
  op = str(input("Select the operator\n +\n -\n *\n /\n "))
  n2 = int(input("Whats your second number\n"))

  a = operation(n1, n2, op)

  print(f"The answer of the operation is {a}\n")

  resume = input("If you want to continue with this answer enter 'y' or if you want to start with calculation enter 'new'\n ")

  while resume == "y":
    b = int(a)
    opp = str(input("Select the operator\n +\n -\n *\n /\n "))
    n22 = int(input("Whats your second number\n"))

    a = operation(b, n22, opp)
    print(f"The answer of the operation is {a}")

    resume = input("If you want to continue with this answer enter 'y' or if you want to start with calculation enter 'new'\n ")

    
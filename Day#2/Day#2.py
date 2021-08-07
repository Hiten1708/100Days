print("Welcome to tip calculator")
bill = float(input("What was the total bill? \n"))
no = int(input("How many people to split the bill? \n"))
tip = float(input("What percentage tip you would like to give? 10, 12, 15?\n"))

fnl_amt = bill + bill*0.01*tip

print("Each person should pay " + str(round(fnl_amt/no, 2)))
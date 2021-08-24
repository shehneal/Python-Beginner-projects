# This program tests the compatibility between two people. It takes both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. For Love Scores **less than 10** or **greater than 90**, the message should be:`"Your score is **x**, you go together like coke and mentos."` For Love Scores **between 40** and **50**, the message should be:`"Your score is **y**, you are alright together."`Otherwise, the message will just be their score. e.g.:`"Your score is **z**."`

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_a = name1.lower()
name_b = name2.lower()

t = name_a.count("t") + name_b.count("t")
r = name_a.count("r") + name_b.count("r")
u = name_a.count("u") + name_b.count("u")
e = name_a.count("e") + name_b.count("e")
true = int(t + r + u + e)

l = name_a.count("l") + name_b.count("l")
o = name_a.count("o") + name_b.count("o")
v = name_a.count("v") + name_b.count("v")
e = name_a.count("e") + name_b.count("e")
love = int(l + o + v + e)

score= (f"{true}{love}")
final_score = int(score)

if final_score < 10 or final_score > 90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")

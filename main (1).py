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
fscore = int(score)

if fscore < 10 or fscore > 90:
  print(f"Your score is {fscore}, you go together like coke and mentos.")
elif fscore >= 40 and fscore <= 50:
  print(f"Your score is {fscore}, you are alright together.")
else:
  print(f"Your score is {fscore}.")


























































#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇


with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:60]
    for x in f2:
      file.write("    " + x)


import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def run_test(self, given_answer, expected_print):
    with patch('builtins.input', side_effect=given_answer), patch('sys.stdout', new=StringIO()) as fake_out: 
      testing_copy.test_func()
      self.assertEqual(fake_out.getvalue(), expected_print) 

  def test_1(self):
    self.run_test(given_answer=['David Beckham', 'Victoria Beckham'], expected_print='Welcome to the Love Calculator!\nYour score is 45, you are alright together.\n')

  def test_2(self):
    self.run_test(given_answer=['Han Solo', 'Princess Leia Organa'], expected_print='Welcome to the Love Calculator!\nYour score is 47, you are alright together.\n')

  def test_3(self):
    self.run_test(given_answer=['Pierre Curie', 'Marie Curie'], expected_print='Welcome to the Love Calculator!\nYour score is 125, you go together like coke and mentos.\n')

  def test_4(self):
    self.run_test(given_answer=['Mark Antony', 'Cleopatra'], expected_print='Welcome to the Love Calculator!\nYour score is 54.\n')


print('\n\n\n.\n.\n.')
print('Checking if your print statements match the instructions. \nFor "Mario" and "Princess Peach" your program should print this line *exactly*:\n')
print('Your score is 43, you are alright together.\n')
print('\nRunning some tests on your code with different name combinations:')
print('.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py') 

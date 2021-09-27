

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
import random
number_list = []

def numbers():
  for number in range(0, 101):
    number_list.append(number)

numbers()
difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ")

if  difficulty_type == 'easy':
  number_of_turns = 10
elif difficulty_type == 'hard':
  number_of_turns = 5
actual_answer = random.choice(number_list)
print(actual_answer)


def compare(): 
  global keep_playing
  player_guess = int(input("Make a guess: "))
  if player_guess < 1 or player_guess > 100:
    print("Your guess is out of range.")
  elif player_guess == actual_answer:
    print(f"You got it! The answer was {actual_answer}.")
    keep_playing = False
  elif player_guess > actual_answer:
    print("Too high.")
  elif player_guess < actual_answer:
    print("Too low.")

keep_playing = True

while keep_playing:
  if number_of_turns == 0:
    keep_playing = False
    print("you ran out of your turns.")
  elif number_of_turns > 0:
    print(f"you've {number_of_turns} turns left.")
    number_of_turns -= 1
    compare()
    

    
    
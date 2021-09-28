from game_data import data
from art import logo, vs
from replit import clear
import random

def options(option_name):
  option = random.choice(data)
  name = option["name"]
  followers = option["follower_count"]
  description = option["description"]
  country_name = option["country"]
  if option_name == "A":
    print(f"Compare {option_name}: {name},  {description}, {country_name}. ")
  elif option_name == "B":
    print(f"Against {option_name}: {name}, {description}, {country_name}. ")
  return followers

def higher_followers(a, b):
  if a > b:
    return a
  elif b > a:
    return b

def player_answer(a, b):
  if player_guess == "A":
    return a
  elif player_guess == "B":
    return b

score = 0
play_game = True

while play_game:
  print(logo)
  if score > 0:
    print(f"You're right! Current score: {score}.")
  followers_a = options("A")
  print(vs)
  followers_b = options("B")
  player_guess = input("Who has more followers? Type 'A' or 'B': ")
  result = higher_followers(followers_a, followers_b)
  guess = player_answer(followers_a, followers_b)
 
  if guess == result:
    score += 1
    clear()
  else:
    play_game = False
    print(f"Sorry, that's wrong. Final score: {score}.") 







# make a compare function 
# ask user to chose an option
# add user points until the user guess is right
#end game when wrong
#print user score 

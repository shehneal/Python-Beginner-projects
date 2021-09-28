from game_data import data
from art import logo, vs
from replit import clear
import random

def higher_followers(option_a, option_b):
  if(option_a[followers] > option_b[followers]):
     return option_a
  elif(option_a[followers] < option_b[followers]:
     return option_b
     

def check_player_answer(guess, correct_option):
  if guess == correct_option[followers]:
    return True
  else:
    return False
  
      
score = 0
play_game = True

while play_game:
  print(logo)
  if score > 0:
    print(f"You're right! Current score: {score}.")
    

  option_a = random.choice(data)
  print(f"Compare {option_name}: {option_a[name]},  {description}, {option_a[country_name]}. vs")
  option_b = random.choice(data)
  print(f"Compare {option_name}: {option_b[name]},  {description}, {option_b[country_name]}. vs")
 
  correct_option = higher_followers(option_a, option_b)
  player_guess = input("Who has more followers? Type 'A' or 'B': ")
  guess = check_player_answer(player_guess, correct_option)
 
  if guess == True:
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

from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
dictionary_of_bids = {}
bidders = True

def highest_bidder(bidding_record):
  max_bid = 0
  for person in dictionary_of_bids:
    if int(dictionary_of_bids[person]) > max_bid:
      max_bid = int(dictionary_of_bids[person])
      winner = person 
  print(f"Winner is {winner}! with a bid of ${max_bid}.")

while bidders:
  name = input("What is your name: ")
  bid = input("What is your bid: $")
  dictionary_of_bids[name] = bid
  more_bidders = input("Are there other users who want to bid? Type 'yes' or 'no'.\n ")
  if more_bidders == "yes":
    clear()
  elif more_bidders == "no":
    bidders = False
    highest_bidder(dictionary_of_bids)




    

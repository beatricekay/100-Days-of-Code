import os #importing os
import logo_art

# Define clear() function
def clear(): # putting it in a function so you can use it many times
  os.system('clear') # clears console

# Define function to find highest bid amount and bidder
def highest_bidder(dictionary):
    # Assume the max bid is 0
    max_bid = 0
    max_bidder = ""
    
    for bidder in bid_dict:

        bid_amount = bid_dict[bidder]

        if bid_amount > max_bid:
            max_bid = bid_amount
            max_bidder = bidder

    print(bid_dict)
    print(f"The highest bid is ${max_bid} by {max_bidder}.")

# Start bidding
print(logo_art.logo)
print("Welcome to the secret auction program.")

bid_dict = {}
continue_bid = True

while continue_bid == True:

    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_dict[name] = bid
    other_bidders = input("Are there any other bidders? Types 'yes' or 'no'.")

    if other_bidders == 'yes':
        continue_bid = True
        clear()
    
    elif other_bidders == 'no':
        continue_bid = False
        highest_bidder(bid_dict)


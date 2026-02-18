# AI: I don't use AI for this task.

import random

# --- 2/17 class insertion sort ---
# best: O(n)
# worst: O(n^2)
# average: O(n^2)
# This algorithm prioritizes space, not time.
def insertion_sort_cards(arr):
    for i in range(1, len(arr)):
        pos = i
        while pos > 0 and arr[pos - 1] > arr[pos]:
            arr[pos], arr[pos - 1] = arr[pos - 1], arr[pos]
            pos -= 1
    return arr

# Initialize Deck 
#SUITS_ORDER = ["Clubs", "Diamonds", "Hearts", "Spades"]
#RANKS_ORDER = ["2", "3", "4", "5", "6", "7", "8",
#               "9", "10", "J", "Q", "K", "A"]
#deck = [(suit, rank) for suit in SUITS_ORDER for rank in RANKS_ORDER]

# In this implementation, all cards are assumed to be numeric. 
# If alphabetic characters are included, a mapping table would be required.
RANKS_ORDER = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
deck = [(rank) for rank in RANKS_ORDER]
random.shuffle(deck)

# initialize Hand. Fist of all we have blank list.
hand = []

# Main process
print("deck:",deck)
print("Start of Process.")
while True:
    # do following repeatedly.
    # 1.user input / draw card
    # 2.sort 
    # 3.show hands

    # 1.user input
    user_input = input("(q is quit, otherwise just enter.)> ")
    if user_input == "q":
        print("Quit")
        break

    # draw card
    if len(deck) == 0:
        print("Deck is empty")
        break
    hand.append(deck.pop())

    # 2.sort 
    hand = insertion_sort_cards(hand)

    # 3.show hands
    print("deck:",deck)
    print("hand:",hand)

print("End of Process.")

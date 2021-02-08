import random

suits = ["Hearts","Spades","Clubs","Diamonds"]
ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')

print(f'There are {len(deck)} card in the deck.')
print('Dealing ...')
hand = []

while len(hand) < 5:
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)

print(f'There are {len(deck)} cards in the deck.')
print('Player has the following cards in their hand:')
print(hand)
'''
There are 52 card in the deck.
Dealing ...
There are 47 cards in the deck.
Player has the following cards in their hand:
['Queen of Clubs', '4 of Clubs', '6 of Diamonds', '8 of Clubs', '5 of Hearts']
'''
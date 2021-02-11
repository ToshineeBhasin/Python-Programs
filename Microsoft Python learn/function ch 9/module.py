#deck module
'''
create your own module to hold one or more functions.
'''

def create_deck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = ["2","3","4","5","6","7","8","9","10","Jack","King","Queen","Ace"]
    deck = []
    
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}') 

    return deck
'''
Created on Oct 23, 2016

@author: Jaime
'''
import Deck

myDeck = Deck.deck()

myDeck.shuffle()

for n in range(0,5):
    print(myDeck.deck[n])




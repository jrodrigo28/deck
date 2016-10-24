'''
Created on Oct 23, 2016

@author: Jaime
'''

from Card import Card
from random import shuffle

class deck():
    def __init__(self):
        self.suits = ["d","c","h","s"]
        self.ranks = range(1,14) #inclusive for loop
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(rank,suit))
                
    def shuffle(self):
        shuffle(self.deck)
    

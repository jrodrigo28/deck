'''
Created on Oct 23, 2016

@author: Jaime
'''

class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        if(self.rank<=10): 
            self.value = self.rank
        else:
            self.value = 10
        
        
    def __repr__(self):
        letters = {1:'A',11:'J',12:'Q',13:'K'}
        letter = letters.get(self.rank,str(self.rank))
        return "<Card %s%s>" % (letter,self.suit) 
        
#Button Class
#Final Project
#Cassandra Lin and Christine Yi
#Due Date: 12/22/2015
#deck.py
#This class represents a deck of cards
from playingcard import *
from random import *

class Deck:

    def __init__(self):
        """Constructor creates a standard deck"""
        #create a new deck of 52 cards in a standard order
        self.cardList = []#instance variable
        cardSuits = ['d','c','h','s']
        for s in cardSuits:#loop through each suit
            for r in range(1,14):#loop through each rank in a suit
                self.cardList.append(PlayingCard(r,s))#create card
    
    def shuffle(self):
        """Shuffle the deck of cards."""
        shuffle(self.cardList)#randomize the order of cards

    def dealCard(self):
        """Returns a single card from the top of the deck and removes it from
           the deck."""
        dealt = self.cardList[0]#deal a card from deck
        del self.cardList[0]#delete that card 
        return dealt
        
        
if __name__ == "__main__": 
   pass
                

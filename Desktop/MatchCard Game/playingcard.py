#PlayingCard Class
#Final Project
#Cassandra Lin and Christine Yi
#Due Date: 12/22/2015
# playingcard.py
#This class creates playing card objects.
from random import randrange

class PlayingCard:
    """This class has the following instance variables:
       rank: an integer 1-13 representing the card value
       suit: a string representing the suit of the card
             'd', 'c', 'h', or 's'"""

    def __init__(self, rank, suit):
        """Creates a playing card, eg:
        d5 = PlayingCard(5, "d") creates the 5 of Diamonds"""
        self.rank = rank #rank is an int in range 1 to 13
        self.suit = suit #suit "d","c","h" or "s"
        self.faceUp = True 

    def getRank(self):#accessor method
        """Returns the rank of the card, an int 1-13"""
        return self.rank #return the rank of the card

    def getSuit(self):#accessor method
        """Returns the suit of the card: 'd', 'c', 'h', or 's'"""
        return self.suit #return the suit of the card

 
            
        





if __name__ == "__main__": 
    main()

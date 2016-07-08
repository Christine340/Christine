#Game Class
#Final Project
#Cassandra Lin and Christine Yi
#Due Date: 12/22/2015
# gameclass.py
#This class simulates a card memory game.
from graphics import *
from deck import *
from random import *
from buttonclass import *
from time import *
from newgrid import *


class Game:
    '''This class has the following methods:
       uncover,cover,checkMatch,deactivate,checkGameOver'''
    def uncover(self,grid,pt):
        '''reveals the card clicked and returns its label and its position in the grid'''

        label = ''#default
        for i in range(grid.numCards):#loop through all buttons in grid
            if grid.bList[i].isClicked(pt):
               grid.coverList[i].undraw()#undraw the one that is clicked
               label = grid.bList[i].getLabel()#get the label
               return label, i
        return -1 #no button clicked

    def cover(self,gwin,grid,pt):
        '''flips over the card so it is face down again'''
        for i in range(grid.numCards):#find the button that is clicked and flip it
            if grid.bList[i].isClicked(pt):
               grid.coverList[i].draw(gwin)  

    def checkMatch(self,grid,pt1,pt2):
        '''Takes in two mouse clicks, returns True if cards match,
           False otherwise''' 
        if self.uncover(grid, pt1) != -1 and self.uncover(grid,pt2) != -1:
            label1, cardID1= self.uncover(grid, pt1)
            label2, cardID2= self.uncover(grid,pt2)

            if cardID1 != cardID2:
                return label1 == label2
        return False
        #return label1 == label2 and cardID1 == cardID2#compare the labels
            

    def deactivate(self,grid,pt):
        '''deactivates the button that is clicked'''
        for i in range(grid.numCards):
            if grid.bList[i].isClicked(pt):#loop through and deactivate the button
               grid.bList[i].deactivate()  #that is clicked

    
    def checkGameOver(self, grid):
        '''returns True if all buttons are deactivated, False otherwise'''
        for i in range(grid.numCards):
            if grid.bList[i].active == True:#if there is still an active button
                return False #game is not over
        return True
        
if __name__ == "__main__": 
    main()
            

        

        

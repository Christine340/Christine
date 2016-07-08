#Button Class
#Final Project
#Cassandra Lin and Christine Yi
#Due Date: 12/22/2015
# button.py
#This class creates buttons
from graphics import *
from deck import *
from random import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """Creates a rectangular button, eg:
           qb = Button(myWin, centerPoint, width, height, 'Quit')
           This class has the following instance variables:
           xmax, ymax = x and y coordinates of one corner of the button
           xmin, ymin are analogous for an opposite corner of the button
           rect = rectangular button constructed from the two corner pts
           label = Text object centered at center point of button"""
        
        w,h = width/2.0, height/2.0 #w = half of the width, h = half of the height 
        x,y = center.getX(), center.getY() #coordinates of the center point
        self.xmax, self.xmin = x+w, x-w #x-coordinates of two corners of the button
        self.ymax, self.ymin = y+h, y-h #y-coordinates of two corners of the button
        p1 = Point(self.xmin, self.ymin) #one of the corner points of the button
        p2 = Point(self.xmax, self.ymax) #opposite corner point 
        self.rect = Rectangle(p1,p2) #rectangle constructed from the two corner points
        self.rect.setFill('lightgray') #sets button color to lightgray
        self.rect.draw(win) #draws button
        self.label = Text(center, label) #text label centered at center point
        self.label.draw(win) #draws label
        self.activate() #sets button to active

        

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2) #set the outline to look bolder
        self.active = True #set the boolean variable that tracks "active"-ness to True

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgray')#color the text "darkgray"
        self.rect.setWidth(1)   #set the outline to look finer/thinner
        self.active = False #set the boolean variable that tracks "active"-ness to False

    def isClicked(self, p):
        """Returns true if button active and Point p is inside"""
        if p is None:
            return False
        else:
            x,y = p.getX(), p.getY()#get user mouse click point
            if self.active == True and self.xmin < x < self.xmax and self.ymin < y < self.ymax:
                return True
            #else, button was not clicked or was not active
            return False

    def setColor(self, color):
        "Sets color of the button."""
        self.rect.setFill(color)#set button rectangle color
    
def main():
    
    win = GraphWin("Button Class", 600,600)
    
    quitButton = Button(win, Point(500, 550), 50, 50, "Quit")
    dealSuits = []
    dealRanks = []

    d = Deck()
    d.shuffle()

    xpos1 = 220
    xpos2 = 300
    ypos1 = 200
    ypos2 = 300
    
    bList = []


    
if __name__ == "__main__": 
    main()

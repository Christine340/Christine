#newgrid Class
#Final Project
#Cassandra Lin and Christine Yi
#Due Date: 12/22/2015
#newgrid.py
#
from graphics import *
from math import *
from buttonclass import *
from deck import *
from time import *


class Grid:
    'This class creates a grid for the memory game.'

    def __init__(self, gwin, level, numCards):
        '''creates a grid of cards based on level'''
        d = Deck()
        d.shuffle()#shuffle the cards
        self.d = d
        self.level = level
        self.numCards = numCards
        self.numRows = sqrt(numCards)
        self.numCols = sqrt(numCards)
        
        dealSuits = [] #empty list to hold the suits of the dealt cards
        dealRanks = [] #holds the ranks of dealt cards       
      
            
        #create grid
        w = int(self.numRows) #number of rows and columns
        if self.level ==1:
            divisions=300/w #divide the window depending on numCards
            a=200 #helps center the grid
            delay=3#delay number of seconds
        elif self.level == 2:  
            divisions = 400/w 
            a=150
            delay=4
        elif self.level==3:
            divisions=600/w
            a=50
            delay=5

        self.delay = delay 
        x = [] #store x-coordinates
        y = [] #store y-coordinates
        coords = [] #store coordinates of midpoints
        used = [] #store coordinates of points already displayed
        

        for i in range(w):
            #creates midpoints for each grid box
            x.append((divisions/2)+(i*divisions) +a)
            y.append((divisions/2)+(i*divisions) +a)
           

        for i in range(w):
            for j in range(w):
                coords.append((x[i], y[j]))#store coordinates of midpoints

        bList = []#holds buttons
        for i in range(numCards//2):

            dealCard = self.d.dealCard()
            
            suit = dealCard.getSuit()#get suit of cards
            rank = dealCard.getRank()#get rank of cards

            dealSuits.append(suit)
            dealRanks.append(rank)
            crank, csuit = rank,suit#create copy of cards
            
            #pick random points to place card and its copy
            pt = randrange(0, len(coords))
            pt2 = randrange(0, len(coords))
            
            #while pt has already been displayed
            #choose a new point
            while pt in used or pt2 in used or pt == pt2: 
                pt = randrange(0, len(coords))
                pt2 = randrange(0,len(coords))
            
            x1,y1 = coords[pt] #get x and y coordinates of the points
            x2, y2 = coords[pt2]

            
            #once point is chosen, add it to used 
            used.append(pt)
            used.append(pt2)

            #get the image of the card chosen
            im = Image(Point(x1,y1),
            "playingcards/" + dealSuits[i] + str(dealRanks[i]) + ".gif")
           #get the copy of the image
            imCopy = Image(Point(x2,y2),
                           "playingcards/" + dealSuits[i] + str(dealRanks[i]) + ".gif")


            currentSuit = dealSuits[i]
            currentRank = str(dealRanks[i])
            currentLabel = currentSuit + currentRank
            
            w = im.getWidth()
            h = im.getHeight()
            #give labels to every button(every card) with its corresponding
            #rank and suit. same for copy cards
            imButton = Button(gwin, Point(x1, y1), w, h, currentLabel)
            copyButton = Button(gwin, Point(x2,y2),w,h,currentLabel)
            bList.append(imButton)#add to list of buttons 
            bList.append(copyButton)

            self.bList = bList
            im.draw(gwin)#draw the card images
            imCopy.draw(gwin)

        sleep(delay)
        coverList=[]
        for i in used:#cover all cards
            cx, cy = coords[i] 
            cover = Image(Point(cx, cy),"playingcards/b2fv.gif")
            coverList.append(cover)
            cover.draw(gwin)
        self.coverList=coverList

        


def coverAll(gwin): #creates rectangle that covers window
    rectangle = Rectangle(Point(0,0), Point(550,550))
    rectangle.draw(gwin)
    rectangle.setFill("pink")
    rectangle.setOutline("pink")
    


if __name__ == "__main__": 
    main()

                
                
            
        
        
        

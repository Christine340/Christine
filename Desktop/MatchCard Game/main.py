#main
#Final Project
#Cassandra Lin and Christine Yi
#Due Date: 12/22/2015
#main.py
#This program simulates a card memory game in a GUI. There are three different
#levels to choose from. 10 points are added for every correct match, and high 
#scores (based on time taken to complete each level) are written to a text file.
#User can also choose to play again.
from graphics import *
from buttonclass import *
from deck import *
from time import *
from newgrid import *
from gameclass import *

def setUp(gwin):
    '''sets up game with title screen and introduction'''
    title=Text(Point(350,150),'Welcome to Memory Game')#create title
    title.setSize(28)#set title size
    title.draw(gwin)#draw title
    description=Text(Point(350,280),"This game includes three difficulty levels.\
You \nwill have a few seconds to memorize the \ncards. \
Then, match the identical pairs.\n You earn 10 points for every correct match.\
\nTry to match them as fast as you can!\nHigh scores will be added to a text \
file.")
    description.draw(gwin)
    gwin.setBackground("pink")#set background color
    
    prompt=Text(Point(350,380),"Click anywhere to begin.")#prompt user to click
    prompt.setSize(15)#set prompt size
    prompt.draw(gwin)#draw prompt
    gwin.getMouse()#get user mouse click
    title.undraw()#undraw title 
    prompt.undraw()#undraw prompt
    description.undraw()

def playAgain(gwin):
    '''allows user to play again by calling main'''
    main()

def main():
    win = GraphWin("Memory game", 700,700) #create a window
    game = Game()#create a game
    setUp(win) #sets up title screen and intro
    prompt1=Text(Point(350,250),"Please choose a difficulty level")
    prompt1.setSize(15)                                     
    prompt1.draw(win)
    #create buttons for each level
    levelOne=Button(win,Point(250,300),50,30,"Easy")
    levelTwo=Button(win,Point(350,300),75,30,'Medium')
    levelThree=Button(win,Point(450,300),50,30,"Hard")

    pt = win.getMouse()#get user mouse click
    prompt1.undraw()#undraw prompt
    
    coverAll(win)#draw a pink rectangle to cover all drawn objects
    quitButton = Button(win, Point(670, 680), 40, 20, "Quit")#create quit button
    #quitButton.deactivate()
    
    prompt2=Text(Point(350,20),'You have a few seconds to memorize the cards')
    prompt2.draw(win)
        
    if levelOne.isClicked(pt):#if each level is clicked
        g = Grid(win, 1,4)#display the corresponding number of cards
        txtfile = "rank1.txt" #text file that contains high scores for level 1
        
    elif levelTwo.isClicked(pt): #easy level: 4 cards
        g = Grid(win, 2,16)       #medium level: 16 cards
        txtfile = "rank2.txt"
        
    elif levelThree.isClicked(pt): #hard level: 36 cards
        g = Grid(win, 3, 36)
        txtfile = "rank3.txt"
        
    else:
        g = Grid(win, 2,16) #default: level 2
        txtfile = "rank2.txt"
    
    #create play again button
    playAgainButton=Button(win,Point(580,680),100,20,"Play Again") 
    playAgainButton.deactivate() 
    score=0 #initialize score
    prompt2.setText("Your score is "+str(score)) #display score

    #start timer
    start = time()
    timeScore = 0
    timeDisplayed = False

    #while quit button is not clicked
    while (not quitButton.isClicked(pt)) or (not quitButton.isClicked(pt2)): 
        try:
            currentTime = time() - start
            #if game is over, activate playAgain button
            if game.checkGameOver(g) and not timeDisplayed:
                timeScore = round(currentTime)
                output = Text(Point(350,40), 'It took you ' + str(timeScore) + ' seconds.')
                output.draw(win)
                playAgainButton.activate()
                timeDisplayed = True

                #update text file containing ranks (high scores)
                updated = checkRank(timeScore, txtfile)
                #if user's rank is a high score
                #add user's rank to the text file
                if checkRank(timeScore, txtfile) != -1: 
                    outputfile = open(txtfile, 'w')
                    for i in updated:
                        outputfile.write(str(i)+ ' ') 
                    outputfile.close()
                    prompt2.setText('New high score added!')

                pt = win.getMouse()

            #close win if playAgain button is clicked
            if playAgainButton.isClicked(pt):
                win.close()
                playAgain(win) #call play again
            #check if quitButton was clicked after each mouse click
            elif quitButton.isClicked(pt): 
                win.close()
                break
                
            pt=win.getMouse()#get user mouse click
            if quitButton.isClicked(pt):
                win.close()
                break
            game.uncover(g, pt) #uncover card after click
            pt2 = win.getMouse()#get second mouse click
            if quitButton.isClicked(pt2):
                win.close()
                break

            if game.checkMatch(g,pt,pt2) == False: 
            #if cards don't match or at least one pt was not a button
                #one button clicked
                if game.uncover(g,pt) != -1 and game.uncover(g,pt2) == -1: 
                    game.cover(win,g,pt)
                elif game.uncover(g,pt2) != -1 and game.uncover(g,pt) == -1:
                    game.cover(win,g,pt2)
                else: #both buttons were clicked
                    sleep(0.5) #wait half a second, then cover the cards again
                    game.cover(win,g,pt)
                    game.cover(win,g,pt2)

            elif game.checkMatch(g,pt,pt2) == True: #cards matched
                game.deactivate(g,pt) #deactivate the buttons once matched
                game.deactivate(g,pt2)
                score+=10 #increment score by 10
            prompt2.setText("Your score is "+str(score))#update score

        except(GraphicsError): #error checking
            #print('Please try again.')
            #break
            pass
    win.close()   




def checkRank(userRank, file):
    '''Returns newRanks if user's time is less than the last rank 
       in text file, -1 otherwise.'''

    inputFile = open(file, 'r') #reads file
    ranks = inputFile.read()
    ranksList = ranks.split() #splits file by spaces
    newRanks = [] #initializes empty list
    for i in ranksList: #converts string to int
        add = int(i)
        newRanks.append(add) #adds int to newRanks

    inputFile.close()
    if newRanks != []:
        lastRank = newRanks[-1]
        if userRank < lastRank: #compare userRank to lastRank
            newRanks.append(userRank)
            newRanks.sort() #sort the updated list
            return newRanks
        else:
            return -1
    else: #nothing in newRanks, so add userRank
        newRanks.append(userRank)
        return newRanks



if __name__ == "__main__": 
    main()
            

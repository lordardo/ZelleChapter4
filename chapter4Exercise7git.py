__author__ = 'aaronhill'

#Instructions:
#Write a program that computes the intersection of a circle with a horizontal line and displays the information textually
#and graphically.
#I chose to randomize the height of the horizontal line.
#https://www.youtube.com/watch?v=c8nBAY9iMKI

#We know that a line equation is y = mx + b.  A horizontal line equation is y = m(0) + b => y = b
#Circle equation is with a center at (a, b)  (x-a)^2 + (y-b)^2 = r^2
#

#Psuedocode
#   Import graphics
#   Import random
#   Import math
#   Create a window that is 600 x 600
#   Draw a circle with center at 300, 300, radius of 200
#   Generate a horizontal line
#   Calculate the intersections
#       Calculate the value of x (solve for its quadratic equation) (should result in two answers)
#       Calculate the value of y
#

import random
import math
from graphics import *

def main():
    win = GraphWin("Line intersecting a circle", 600, 600)
    win.setBackground("white")

    #create the larger circle and the centerpoint (cenerpoint is for reference for me)
    center = Point(300, 300)
    c = Circle(center, 200)
    c.setFill("white")
    c.setOutline("blue")
    c.setWidth(5)
    c.draw(win)

    centerPoint = Circle(Point(center.getX(), center.getY()), 5)
    centerPoint.draw(win)

    #generate where the line is on the y axis randomly
    yIntercept = random.randint(80, 400)

    #draw the line
    l = Line(Point(0, yIntercept), Point(600, yIntercept))
    l.setWidth(5)
    l.draw(win)


    a = math.sqrt((c.getRadius()^2) - ((center.getY() - yIntercept)^2))

        #get the distance from the left edge of window until first circle/line intercept

    d = (600 - (a*2)) / 2


    p1 = Point(0 + d, yIntercept)
    p2 = Point((600 - d), yIntercept)

        #print the results
        #for now I'm going to be cheap and print it in the terminal
    print("Point 1 is at: ", p1.getX(), ",", p1.getY())
    print("Point 2 is at: ", p2.getX(), ",", p2.getY())

    tp1x = Text(Point(150, 25), p1.getX())
    tp1x.setSize(25)
    tp1x.draw(win)
    tp1y = Text(Point(300, 25), p1.getY())
    tp1y.setSize(25)
    tp1y.draw(win)

    tp2x = Text(Point(150, 50), p2.getX())
    tp2x.setSize(25)
    tp2x.draw(win)
    tp2y = Text(Point(300, 50), p2.getY())
    tp2y.setSize(25)
    tp2y.draw(win)


    #wait for mouse click to close
    win.getMouse()
    win.close()

main()
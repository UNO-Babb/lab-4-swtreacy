#TurtleGraphics.py
#Name: Sean Treacy
#Date: 9/22/24
#Assignment: Turtle Graphics.py

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)

def fillCorner(dave, corner):
    #draw big square
    drawSquare(dave, 100)
    
    if corner == 1:
        dave.begin_fill()
        drawSquare(dave, 50)
        dave.end_fill()
    elif corner == 2:
        dave.penup()
        dave.forward(50)
        dave.pendown()
        dave.begin_fill()
        drawSquare(dave, 50)
        dave.end_fill()
    elif corner == 3:
        dave.penup()
        dave.right(90)
        dave.forward(50)
        dave.left(90)
        dave.pendown()
        dave.begin_fill()
        drawSquare(dave, 50)
        dave.end_fill()
    elif corner == 4:
        dave.penup()
        dave.forward(50)
        dave.right(90)
        dave.forward(50)
        dave.left(90)
        dave.pendown()
        dave.begin_fill()
        drawSquare(dave, 50)
        dave.end_fill()

def squaresInSquares(chet, squares):
    chet.up()
    chet.goto(-200,200)
    chet.down()
    for s in range(squares):
        drawSquare(chet, 40 * squares)
        chet.up()
        chet.forward(20)
        chet.right(90)
        chet.forward(20)
        chet.left(90)
        chet.down()
        squares = squares - 1
       
        


def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()

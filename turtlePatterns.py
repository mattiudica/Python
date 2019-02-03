import turtle
import time

t=turtle.Turtle()
ts=turtle.getscreen()
ts.bgcolor("blue")
# t.pencolor("white")
# t.pensize(0.7)
ts.colormode("255")


lengthList = [100,75,50,25]

def createSqr(length):

	for i in range(4):
		t.forward(length)
		time.sleep(0.5)
		t.left(90)
def createPatern():
	t.pencolor("white")
	t.pensize(5)
	for i in lengthList:
		lenthVal = i
		createSqr(lenthVal)
	t.left(45)
	t.forward(165)
		


def drawShape(n):
	for i in range(n):
		t.forward(50)
		angle = (180 *(n-2))/n
		t.left(180-angle)
def drawPattern():
	t.pencolor("yellow")
	t.pensize(0.7)
	for i in range(3,11):
		drawShape(i)


def drawRomboid():
	t.pencolor("red")
	t.pensize(0.7)
	t.forward(100)
	t.left(120)
	time.sleep(1)
	t.forward(100)
	t.left(120)
	time.sleep(1)
	t.forward(100)
	t.left(60)
	time.sleep(1)
	t.forward(100)
	t.left(120)
	time.sleep(1)
	t.forward(100)

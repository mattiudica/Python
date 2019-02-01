import turtle
import time


t=turtle.Turtle()
ts=turtle.getscreen()
ts.bgcolor("blue")
t.pencolor("white")
t.pensize(5)
ts.colormode("255")

lengthList = [100,75,50,25]

def createSqr(length):

	for i in range(4):
		t.forward(length)
		time.sleep(0.5)
		t.left(90)

def createPatern():
	for i in lengthList:
		lenthVal = i
		createSqr(lenthVal)
	t.left(45)
	time.sleep(0.8)
	t.forward(165)
		
createPatern()



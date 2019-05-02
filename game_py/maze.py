import turtle
import time
import math
import winsound
import random



#SCREEN-BACKGROUND SETUP
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(700,700)
wn.tracer(0)


#REGISTER THE SHAPES THAT WE LOAD
images = ["image/coin_static.gif",
	"image/wizard_side_left.gif","image/wizard_side_right.gif",
	"image/wizard_front.gif","image/wizard_back.gif",
	"image/stone_wall.gif","image/door_close.gif",
	"image/door_open.gif","image/chest_open.gif","image/chest_closed.gif",
	"image/monster_front.gif","image/monster_right.gif",
	"image/monster_back.gif","image/monster_left.gif"
]
for image in images:
	turtle.register_shape(image)


class Pen(turtle.Turtle):

	def __init__(self):		
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("white")
		self.penup()
		self.speed(0)


class Player(Pen):
	def __init__(self):		
		turtle.Turtle.__init__(self)
		self.shape("image/wizard_side_left.gif")
		# self.color("blue")
		self.penup()
		self.speed(0)
		self.treasures = 0


	def go_down(self):
		move_to_x = player.xcor()
		move_to_y = player.ycor() - 24
		if (move_to_x,move_to_y) not in walls + backpack:
			self.shape("image/wizard_front.gif")
			self.goto(move_to_x,move_to_y)
			winsound.PlaySound("music/moveturtle.wav", winsound.SND_ASYNC)

		else:
			winsound.PlaySound("music/wallcollision.wav", winsound.SND_ASYNC)		


	def go_up(self):
		move_to_x = player.xcor()
		move_to_y = player.ycor() + 24
		if (move_to_x,move_to_y) not in walls + backpack:
			self.shape("image/wizard_back.gif")
			self.goto(move_to_x,move_to_y)
			winsound.PlaySound("music/moveturtle.wav", winsound.SND_ASYNC)
		else:
			winsound.PlaySound("music/wallcollision.wav", winsound.SND_ASYNC)

	def go_left(self):
		move_to_x = player.xcor() - 24
		move_to_y = player.ycor()
		if (move_to_x,move_to_y) not in walls + backpack:
			self.shape("image/wizard_side_left.gif")
			self.goto(move_to_x,move_to_y)
			winsound.PlaySound("music/moveturtle.wav", winsound.SND_ASYNC)
		else:
			winsound.PlaySound("music/wallcollision.wav", winsound.SND_ASYNC)


	def go_right(self):
		move_to_x = player.xcor() + 24
		move_to_y = player.ycor()
		if (move_to_x,move_to_y) not in walls + backpack:
			self.shape("image/wizard_side_right.gif")
			self.goto(move_to_x,move_to_y)
			winsound.PlaySound("music/moveturtle.wav", winsound.SND_ASYNC)
		else:
			winsound.PlaySound("music/wallcollision.wav", winsound.SND_ASYNC)

	def is_collision(self, other):
		a = self.xcor() - other.xcor()
		b = self.ycor() - other.ycor()
		distance = math.sqrt((a ** 2) + (b ** 2))

		if distance < 5:
			return True
		else:
			return False


class Enemie(turtle.Turtle):
	def __init__(self,x,y):
		turtle.Turtle.__init__(self)
		self.penup()
		self.shape("image/monster_front.gif")
		self.speed(0)
		self.goto(x,y)
		self.direction = random.choice(["up","down","left","right"])

	def move(self):
		if self.direction == "up":
			self.shape("image/monster_back.gif")
			dx = 0
			dy = 24
		if self.direction == "down":
			self.shape("image/monster_front.gif")
			dx = 0
			dy = -24
		if self.direction == "left":
			self.shape("image/monster_left.gif")
			dx = -24
			dy = 0
		if self.direction == "right":
			self.shape("image/monster_right.gif")
			dx = 24
			dy = 0

		
		move_to_x = self.xcor() + dx
		move_to_y = self.ycor() + dy

		if (move_to_x,move_to_y) not in walls + backpack:
			self.goto(move_to_x,move_to_y)
		else:
			self.direction = random.choice(["up","down","left","right"])

		turtle.ontimer(self.move, t=random.randint(100, 300))

	def destroy(self):
		self.goto(2000,2000)
		self.hideturtle()




class Treasure(turtle.Turtle):
	def __init__(self,x,y):
		turtle.Turtle.__init__(self)
		self.penup()
		self.shape("image/chest_closed.gif")
		self.speed(0)
		self.goto(x,y)
		self.treasure_count = 1

	def open(self):
		self.shape("image/chest_open.gif")


class Exit(turtle.Turtle):
	def __init__(self,x,y):
		turtle.Turtle.__init__(self)
		self.penup()
		self.goto(x,y)	
		self.shape("image/door_close.gif")
		self.speed(0)
		




mazeGrid = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X      E               DX",
"XXXXXXXXXXXXXXXX  XXXXXXX",
"XXB      X        X E  XX",
"XX   XXXXX XXXX   X    XX",
"XX   XXXXX XXXX   X    XX",
"XX     E          X    XX",
"XXXXXXXXX  XXXXXXXX    XX",
"XX   XXXX              XX",
"XX   XXXX  XXXXXXXX    XX",
"XX      E              XX",
"XXXXXXXXXXX  XXXXXXXX  XX",
"XXXXXX       X         XX",
"XX      XXXXXX         XX",
"XXXXXX  XXXXXXXXXXXXX  XX",
"XXXXXX           XB    XX",
"XXXXXXXXXXXXX    XXXXXXXX",
"X         E            XX",
"X XXXXXXXXXXXXXXXXXXXX XX",
"X             XX       XX",
"XXXXXXXXXXX   XXXXXXX  XX",
"XX      E              XX",
"XX   XXXXXX   XXXXXXXXXXX",
"XX          P          XX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]


def setupMaze(grid):
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			character = grid[x][y]
			screen_x = -288 + (x * 24)
			screen_y = 288 - (y * 24)

			if character == 'P':
				player.goto(screen_x, screen_y)

			if character == 'X':
				pen.goto(screen_x, screen_y)
				pen.shape("image/stone_wall.gif")
				pen.stamp()
				walls.append((screen_x, screen_y))

			if character == 'B':
				backpack.append(Treasure(screen_x,screen_y))
			
			if character == 'E':
				enemies.append(Enemie(screen_x,screen_y))

			if character == 'D':
				global exit
				exit = Exit(screen_x,screen_y)
				walls.append((screen_x, screen_y))



pen = Pen()

player = Player()

walls = []

backpack = []

enemies = []

setupMaze(mazeGrid)

turtle.listen()
turtle.onkeypress(player.go_down, "Down")
turtle.onkeypress(player.go_up, "Up")
turtle.onkeypress(player.go_left, "Left")
turtle.onkeypress(player.go_right, "Right")

for enemie in enemies:
	turtle.ontimer(enemie.move, t=250)
	if player.is_collision(enemie):
		print("You have lost one life!")

wn.tracer(0)

while True:
	for treasure in backpack:
		if player.is_collision(treasure):
			winsound.PlaySound("music/coincollision.wav", winsound.SND_ASYNC)
			player.treasures += treasure.treasure_count
			treasure.open()
			backpack.remove(treasure)
	if player.treasures == 2 and player.is_collision(exit):
		winsound.PlaySound("music/mazesound.wav", winsound.SND_ASYNC)
		turtle.Screen().bye()



	wn.update()


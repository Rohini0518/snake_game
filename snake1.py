import turtle
import random
import time

SNK_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_FRWD=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake():
    def __init__(self):
        self.allturtles=[]
        self.create_snakeblocks()
        self.head=self.allturtles[0]
    def create_snakeblocks(self):
        for i in range(len(SNK_POSITIONS)):
            tim=turtle.Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.goto(SNK_POSITIONS[i])
            # increment-=20
            self.allturtles.append(tim)

    def move(self):
        for tur_num in range(len(self.allturtles)-1,0,-1):
                new_x=self.allturtles[tur_num-1].xcor()
                new_y=self.allturtles[tur_num-1].ycor()
                self.allturtles[tur_num].goto(new_x,new_y)
        self.head.forward(MOVE_FRWD)

    def up(self):
        if self.head.heading()!=DOWN:        
           self.head.setheading(UP)
    def down(self): 
        if self.head.heading()!=UP:         
           self.head.setheading(DOWN)    
    def left(self):
        if self.head.heading()!=RIGHT:          
           self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:         
           self.head.setheading(RIGHT)        

        










# import turtle
from turtle import Screen
import time
from snake1 import Snake
from food import Food
from scoreboard import Scoreboard


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# food.hideturtle()

is_gameon=True
while is_gameon:
    screen.update() 
    time.sleep(0.4)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        score.addscore()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280 : 
        is_gameon=False
        score.gameover()  
        
    
    
  
    











screen.exitonclick()
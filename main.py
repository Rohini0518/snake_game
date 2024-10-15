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



 
is_gameon=True
while is_gameon:
    screen.update() 
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend_snaketail()
        score.addscore()
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285 : 
        is_gameon=False
        score.gameover()
    if snake.body_hits():     
        is_gameon=False
        score.gameover() 
    
    score.highest_score()    




screen.exitonclick()
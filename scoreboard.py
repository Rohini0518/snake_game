from turtle import Turtle
SCR_ALIGNMENT="center"
SCR_FONT=("Courier",18,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270) 
        self.scorewrite()    
        self.hideturtle()
       
    def scorewrite(self):         
        self.write(f"Score :{self.score} ",move=False,align=SCR_ALIGNMENT,font=SCR_FONT)
        
    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over !! ",move=False,align=SCR_ALIGNMENT,font=SCR_FONT)
        

    def addscore(self):
         self.score+=1
         self.clear()
         self.scorewrite()   

        
            
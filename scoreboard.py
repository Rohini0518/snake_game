from turtle import Turtle
SCR_ALIGNMENT="center"
SCR_FONT=("Courier",18,"normal")


with open("scoredata.txt", "r") as f:
    value = int(f.read())
    
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=value
        self.color("white")
        self.penup()
        self.goto(0,270) 
        self.scorewrite()    
        self.hideturtle()
       
        
    def scorewrite(self):         
        self.write(f"Score :{self.score} Highscore:{value}",move=False,align=SCR_ALIGNMENT,font=SCR_FONT)
    
        
    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over !! ",move=False,align=SCR_ALIGNMENT,font=SCR_FONT)
        
    def highest_score(self):
        if self.score>self.highscore:
        #    print(f"scoregrester than highscore={self.score,self.highscore}")
           self.highscore=self.score
           with open("scoredata.txt","w") as f:
              filescore=f.write(str(self.score))  
       
    def addscore(self):
         self.score+=1
         self.clear()
        #  self.highest_score()
         self.scorewrite()   
         
         

        
            
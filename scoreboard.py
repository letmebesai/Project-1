#scoreboard for the snake game to keep track of the score
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score =0
        self.goto(0, 250)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial",10,"normal"))
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0,250)
        self.write(f"Score: {self.score}", align="center", font=("Arial",10))
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= "center", font= ("Arial", 40,"normal"))
        

    

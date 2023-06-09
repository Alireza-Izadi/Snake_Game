from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.add_score()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font= FONT)
        
        
    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score {self.score - 1}", align=ALIGNMENT, font= FONT)
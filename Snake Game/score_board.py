from turtle import Turtle


FONT = ('courier', 20, 'italic')
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # self.high_score = 0
        with open("score_data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"SCORE : {self.score} HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()

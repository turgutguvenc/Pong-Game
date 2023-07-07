from turtle import Turtle

ALINGMENT = "center"
FONT: tuple[str, int, str] = ('Arial', 50, 'normal')


class ScoreBoard(Turtle):
    """
    This class represents the scoreboard in the game.

    Attributes:
        l_score (int): Left player's score.
        r_score (int): Right player's score.

    Methods:
        update_scoreboard(): Update the scoreboard with the current scores.
        l_point(): Increment the left player's score by 1 and update the scoreboard.
        r_point(): Increment the right player's score by 1 and update the scoreboard.
    """

    def __init__(self):
        """
        Initializes a new instance of the ScoreBoard class.
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the scoreboard with the current scores.
        """
        self.clear()
        self.goto(x=-100, y=200)
        self.write(align=ALINGMENT, arg=self.l_score, font=FONT)
        self.goto(x=100, y=200)
        self.write(align=ALINGMENT, arg=self.r_score, font=FONT)

    def l_point(self):
        """
        Increment the left player's score by 1 and update the scoreboard.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Increment the right player's score by 1 and update the scoreboard.
        """
        self.r_score += 1
        self.update_scoreboard()
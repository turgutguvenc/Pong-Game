from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Paddle(Turtle):
    """
    This class represents a paddle in a game.

    Methods:
        up(): Move the paddle up by a fixed distance.
        down(): Move the paddle down by a fixed distance.
    """

    def __init__(self, position):
        """
        Initializes a new instance of the Paddle class.

        Args:
            position (tuple): The initial position of the paddle.

        """
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed('fastest')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        """
        Move the paddle up by a fixed distance.

        The paddle's y-coordinate is increased by the MOVE_DISTANCE.

        """
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        """
        Move the paddle down by a fixed distance.

        The paddle's y-coordinate is decreased by the MOVE_DISTANCE.

        """
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
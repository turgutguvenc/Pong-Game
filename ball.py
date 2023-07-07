from turtle import Turtle

class Ball(Turtle):
    """
    This class represents a ball in the game.

    Attributes:
        x_move (int): The horizontal movement distance of the ball.
        y_move (int): The vertical movement distance of the ball.
        move_speed (float): The speed at which the ball moves.

    Methods:
        move(): Move the ball based on its current x_move and y_move values.
        bounce_y(): Reverse the direction of the ball's vertical movement.
        bounce_x(): Reverse the direction of the ball's horizontal movement and adjust the move speed.
        reset_position(): Reset the ball's position and move speed.

    """

    def __init__(self, position):
        """
        Initializes a new instance of the Ball class.

        Args:
            position (tuple): The initial position of the ball.

        """
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.goto(position)
        self.shapesize()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """
        Move the ball based on its current x_move and y_move values.

        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Reverse the direction of the ball's vertical movement.

        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverse the direction of the ball's horizontal movement and adjust the move speed.

        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """
        Reset the ball's position and move speed.

        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
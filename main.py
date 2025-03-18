from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)



#create the paddles at specific locations
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
top_paddle = Paddle((0, 280))



#add keyboard controls

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")





ball = Ball()
scoreboard = Scoreboard()

is_game_true = True


while is_game_true:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #detect collision with paddles
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    

    #detect when the ball geos out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.player1_score += 1
        scoreboard.clear()
        scoreboard.write(f"{scoreboard.player1_score}  {scoreboard.player2_score}", align="center", font=("Courier", 24, "normal"))
    
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.player2_score += 1
        scoreboard.clear()
        scoreboard.write(f"{scoreboard.player1_score}  {scoreboard.player2_score}", align="center", font=("Courier", 24, "normal"))











screen.exitonclick()
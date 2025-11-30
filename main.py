from turtle import Screen
from paddleClass import Paddle
from ball import Ball
import time
from ScoreBoard import score_board

import paddleClass
print("Imported paddleClass from:", paddleClass.__file__)

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800 ,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350 , 0))
l_paddle = Paddle((-350 , 0))
ball = Ball()
ScoreBoard = score_board()

screen.listen()
screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down , "s")
screen.onkey(r_paddle.go_up , "Up")
screen.onkey(r_paddle.go_down , "Down")

game_is_on = True

while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  if ball.ycor() > 280 or ball.ycor() < -270:
    ball.bounce_y()

  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()
  
  #detect r_positon misses
  if ball.xcor() > 380:
    ball.reset_position()
    ScoreBoard.L_point()

 # detect L_position misses
  if ball.xcor() < -380:
    ball.reset_position()
    ScoreBoard.r_point()
    
screen.exitonclick()



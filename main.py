from turtle import Screen, Turtle, distance
import random
import time
from scoreboard import Scoreboard
from snake import Snake
from Food import Food
my_screen= Screen()
my_screen.setup(width=500, height=500)
my_screen.bgcolor('black')
my_screen.title("THE SNAKE GAME")

starting_positions= ((-40,0),(-20,0),(0,0))
segments=[]
snake_food = Food()
snake_score = Scoreboard()

my_snake=Snake()
my_screen.listen()
my_screen.onkey(my_snake.Up,"Up")
my_screen.onkey(my_snake.Down, "Down")
my_screen.onkey(my_snake.Right,"Right")
my_screen.onkey(my_snake.Left,"Left")

game_is_on=True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    my_snake.move_snake()

    #Detect Collision with food 
    if my_snake.segments[0].distance(snake_food) < 15:
     print("Bingoo!!!!!!!!")
     #increase the length of snake and score of snake by 1
     my_snake.extend()

     snake_score.increase_score()
     snake_food.refresh()
    #detect collision with wall
    if my_snake.segments[0].xcor()>250 or my_snake.segments[0].xcor()<-250 or my_snake.segments[0].ycor()>250 or my_snake.segments[0].ycor()<-250:
       game_is_on=False
       snake_score.game_over()
    #detect collision with tail
    for segment in my_snake.segments[1:]:
       if my_snake.segments[0].distance(segment)<10:
          game_is_on=False
          snake_score.game_over()







































my_screen.exitonclick()
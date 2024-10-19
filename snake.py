from turtle import Turtle, distance

starting_positions = ((0, 0), (-20, 0), (-40, 0))
Move_size=20
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        

    def create_snake(self):
        for i in starting_positions:
            self.add_segment(i)
    
    def add_segment(self,i):
        new_tim = Turtle("circle")
        new_tim.color("White")
        new_tim.penup()
        new_tim.goto(i)
        self.segments.append(new_tim)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
            self.segments[i].penup()
        self.segments[0].forward(Move_size)
    def Up(self):
            #snake can't go down if pointing up
            if self.segments[0].heading()!=270:
                self.segments[0].setheading(90)
            
    def Down(self):
        #snake can't go up if pointing down
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)


    def Right(self):
        #snake can't go left if pointing right
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)

        

    def Left(self):
        #snake can't go right if pointing left
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)



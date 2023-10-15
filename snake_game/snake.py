from turtle import  Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():

    def __init__(self):
        self.segments = []
        self.set_up_snake()
        self.head = self.segments[0]
    
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        
        self.segments.append(new_segment)

    def set_up_snake(self):
        for position in STARTING_POSITIONS:
            # add segments to the current instance of the snake class
            self.add_segment(position)

    def extend(self):
        # add a new segment to the snake once it eats
        self.add_segment(self.segments[-1].position())

    def move(self):
        # all the segments of the snake will follow its head
        for seg_num in range(len(self.segments)-1, 0, -1):

            # get the position of the segment in front of this segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            
            # move to the position of the segment in front of you
            self.segments[seg_num].goto(new_x, new_y)

        # move the first segment
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        "move the snake upwards"

        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move()
    
    def down(self):
        "move the snake downwards"

        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move()

    def right(self):
        "move the snake to the right"
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move()

    def left(self):
        "move the snake to the lefts"

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move()


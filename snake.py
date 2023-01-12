from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (20, 0), (40, 0)]
MOVE_DISTANCE = 20
TURN_ANGLE = 90
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
GAME_OVER = "PLAY"

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            # print("SEgments: ",self.segments)
    
    def increase(self):
        new_x = self.segments[len(self.segments) - 1].xcor()
        new_y = self.segments[len(self.segments) - 1].ycor()
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto((new_x, new_y))
        self.segments.append(new_segment)
        # print("new Segments: ",self.segments)
    

    def move(self):
            
            # To implement the behaviour where the snake can turn with the other segments connected,
            # we need to make sure the segments are linked to one another.

            # One way to do this is to start from the last segment and move it in the place of the second last segment
            # Then, move the second last segment to the third last segment and so on until to you reach the first segment, the head.
            # At this point, the head can turn in any direction and the same process will continue to repeat until the game ends.
            
            for seg_num in range(len(self.segments) - 1, 0, -1):
                x = self.segments[seg_num - 1].xcor()
                y = self.segments[seg_num - 1].ycor()
               
                self.segments[seg_num].goto(x, y)
                
                # if self.segments[seg_num].xcor() > 600:
                #     self.segments[seg_num].xcor() = -600

            self.head.forward(MOVE_DISTANCE)
            
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != UP:   
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != RIGHT:   
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:   
            self.head.setheading(0)
            
    # def collision_with_itself(self):
        

            # print("NEWWWWWWWWW")
            # print(f"x = {x}")
            # print(f"y = {y}")
            # print(f"head x = {self.head.xcor()}")
            # print(f"head y = {self.head.ycor()}")
            
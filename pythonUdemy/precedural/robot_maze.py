import turtle
import math
from typing import List, Tuple

# Set up the screen
wn = turtle.Screen()
wn.title("Robot Maze Solver")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)

# Maze dimensions and properties
step_size = 24  # The size of each movement step
walls: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []  # List to store wall positions

# Create the maze
def setup_maze() -> None:
    global walls
    maze_drawer = turtle.Turtle()
    maze_drawer.hideturtle()
    maze_drawer.penup()
    maze_drawer.speed(0)
    maze_drawer.pensize(3)
    maze_drawer.color("black")

    # Define maze walls (x1, y1, x2, y2)
    maze_walls = [
        # Outer walls
        (-288, -288, 288, -288),
        (288, -288, 288, 288),
        (288, 288, -288, 288),
        (-288, 288, -288, -288),
        # Inner walls (example)
        (-72, -288, -72, 72),
        (72, -72, 72, 288),
        (-72, 72, 72, 72),
        (72, -72, 72, -288),
    ]

    for wall in maze_walls:
        x1, y1, x2, y2 = wall
        maze_drawer.penup()
        maze_drawer.goto(x1, y1)
        maze_drawer.pendown()
        maze_drawer.goto(x2, y2)
        # Store wall positions
        walls.append(((x1, y1), (x2, y2)))

# Create the robot
robot = turtle.Turtle()
robot.shape("turtle")
robot.color("blue")
robot.penup()
robot.speed(0)
robot.setheading(90)  # Facing upward
robot.goto(-264, -264)  # Starting position

# Define the goal
goal = turtle.Turtle()
goal.shape("circle")
goal.color("green")
goal.penup()
goal.goto(264, 264)
goal.stamp()

# Functions to move the robot
def move_forward() -> None:
    if front_is_clear():
        robot.forward(step_size)

def move_backward() -> None:
    robot.backward(step_size)

def turn_left() -> None:
    robot.left(90)

def turn_right() -> None:
    robot.right(90)

def at_goal() -> bool:
    return robot.distance(goal) < step_size / 2

def front_is_clear() -> bool:
    return is_path_clear(robot.heading())

def is_path_clear(heading: float) -> bool:
    x, y = robot.position()
    angle_rad = math.radians(heading)  # Use math.radians() to convert degrees to radians
    dx = step_size * math.cos(angle_rad)
    dy = step_size * math.sin(angle_rad)
    next_x = x + dx
    next_y = y + dy

    # Check for collision with walls
    for wall in walls:
        (x1, y1), (x2, y2) = wall
        if line_intersects_rectangle(next_x, next_y, x1, y1, x2, y2):
            return False
    return True

def line_intersects_rectangle(x: float, y: float, x1: float, y1: float, x2: float, y2: float) -> bool:
    # Define the rectangle boundaries
    left = min(x1, x2) - step_size / 2
    right = max(x1, x2) + step_size / 2
    bottom = min(y1, y2) - step_size / 2
    top = max(y1, y2) + step_size / 2
    # Check if the point is within the rectangle
    return left <= x <= right and bottom <= y <= top

# Set up the maze
setup_maze()
wn.update()

# Keyboard bindings for player control
wn.listen()
wn.onkey(move_forward, "Up")    # Move forward with the "Up" arrow
wn.onkey(turn_left, "Left")     # Turn left with the "Left" arrow
wn.onkey(turn_right, "Right")   # Turn right with the "Right" arrow
wn.onkey(move_backward, "Down") # Move backward with the "Down" arrow

# Game loop to constantly check for updates and goal detection
def game_loop():
    wn.update()  # Refresh the screen
    if at_goal():
        print("Congratulations! You've reached the goal!")
        robot.hideturtle()
    else:
        wn.ontimer(game_loop, 100)  # Keep looping every 100ms

# Start the game loop
game_loop()

# Keep the window open
wn.mainloop()

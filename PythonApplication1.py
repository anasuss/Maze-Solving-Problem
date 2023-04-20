
from collections import deque
import queue
import turtle                    # import turtle library
import time


wn = turtle.Screen()                      # define the turtle screen
wn.bgcolor("black")                       # set the background colour
wn.title("A Maze Solving Program")
wn.setup(1300,700)                        # setup the dimensions of the working window

# declare system variables
start_x = 0
start_y = 0
end_x = 0
end_y = 0

# the five classes below are drawing turtle images to construct the maze.

# use white turtle to stamp out the maze
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("white")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)                   # define the animation speed

# use green turtles to show the visited cells
class Green(turtle.Turtle):               # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

# use blue turtle to show the frontier cells and to draw shortest path 
class Blue(turtle.Turtle):               # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

# use the red turtle to represent the start position
class Red(turtle.Turtle):                # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.setheading(270)  # point turtle to point down
        self.penup()
        self.speed(0)

# use the yellow turtle to represent the end position
class Yellow(turtle.Turtle):           # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

grid4 = [
    "+++++++++++++++",
    "     +        e",
    "               ",
    "      +        ",
    "    +          ",
    "      +        ",
    "         +     ",
    "   +           ",
    "s              ",
    "+++++++++++++++",
]

grid2 = [
"+++++++++++++++",
"+s+       + +e+",
"+ +++++ +++ + +",
"+ + +       + +",
"+ +   +++ + + +",
"+ + + +   + + +",
"+   + + + + + +",
"+++++ + + + + +",
"+     + + +   +",
"+++++++++++++++",
 ]

grid3 = [
"+++++++++",
"+ ++ ++++",
"+ ++ ++++",
"+ ++ ++++",
"+s   ++++",
"++++ ++++",
"++++ ++++",
"+      e+",
"+++++++++",
 ]

grid1 = [
"++++++++++++++++++++++++++++++++++++++++++++++",
"+ s             +                            +",
"+ +++++++++++ +++++++++++++++ ++++++++ +++++ +",
"+           +                 +        +     +",
"++ +++++++ ++++++++++++++ ++++++++++++++++++++",
"++ ++    + ++           + ++                 +",
"++ ++ ++ + ++ ++ +++++ ++ ++ +++++++++++++++ +",
"++ ++ ++ + ++ ++ +     ++ ++ ++ ++        ++ +",
"++ ++ ++++ ++ +++++++++++ ++ ++ +++++ +++ ++ +",
"++ ++   ++ ++             ++          +++ ++e+",
"++ ++++ ++ +++++++++++++++++ +++++++++++++++ +",
"++    + ++                   ++              +",
"+++++ + +++++++++++++++++++++++ ++++++++++++ +",
"++ ++ +                   ++          +++ ++ +",
"++ ++ ++++ ++++++++++++++ ++ +++++ ++ +++ ++ +",
"++ ++ ++   ++     +    ++ ++ ++    ++     ++ +",
"++ ++ ++ +++++++ +++++ ++ ++ +++++++++++++++ +",
"++                     ++ ++ ++              +",
"+++++ ++ + +++++++++++ ++ ++ ++ ++++++++++++++",
"++++++++++++++++++++++++++++++++++++++++++++++",
 ]

# this function constructs the maze based on the grid type above
def setup_maze(grid):                          # define a function called setup_maze
    global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
    for y in range(len(grid)):                 # iterate through each line in the grid
        for x in range(len(grid[y])):          # iterate through each character in the line
            time.sleep(0) 
            character = grid[y][x]             # assign the variable character to the y and x positions of the grid
            screen_x = -600 + (x * 24)         # move to the x location on the screen staring at -600
            screen_y = 288 - (y * 24)          # move to the y location of the screen starting at 288

            if character == "+":                   # if character contains a '+'
                maze.goto(screen_x, screen_y)      # move pen to the x and y location and
                maze.stamp()                        # stamp a copy of the white turtle on the screen
                walls.append((screen_x, screen_y)) # add cell to the walls list

            if character == " ":                    # if no character found
                path.append((screen_x, screen_y))   # add to path list

            if character == "e":                    # if cell contains an 'e'
                yellow.goto(screen_x, screen_y)     # move pen to the x and y location and
                yellow.stamp()                      # stamp a copy of the yellow turtle on the screen
                end_x, end_y = screen_x, screen_y   # assign end locations variables to end_x and end_y
                path.append((screen_x, screen_y))   # add cell to the path list

            if character == "s":                       # if cell contains a "s"
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)           # send red turtle to start position



#Depth-first search
def dfs(x,y):
    global found                    # found is used to indicate if we reach the end cell or not 
    if (found == 1):
        return 
    visited.add((x,y))           # add current cell to visited list
    green.goto(x,y)                 # green turtle goto x and y position
    green.stamp()                   # stamp a copy of the green turtle on the maze 
    if (x == end_x and y == end_y):
        found = 1                   #end cell found
        return ; 
    for i in range(4): #check UP/DOWN/LEFT/RIGHT 
        child = (x+dx[i],y+dy[i]) 
        if (child) in path and (child) not in visited and not found: #check child
            blue.goto(child) # blue turtle goto child 
            blue.stamp()
            dfs(x+dx[i],y+dy[i])
       

#Breadth-First search to find shortest path 
def BFS(x , y):
    global found 
    pred[(x,y)] = -1 
    queue.append((x,y))
    while len(queue)>0 and found == 0:          # as long as we don't reach the end or exist path 
        (x,y) = queue.pop(0)
        parent = (x,y)                         #current cell
        for i in range(4):
            child = (x+dx[i],y+dy[i])          #neighbor cell
            if (child) in path and (child)  not in visited: #check child 
                pred[child] = parent 
                queue.append(child) 
                visited.add(child) 
                if (child == (end_x,end_y)):
                    found = 1
                    break
    shortestPath = deque()
    cell = (end_x,end_y)
    while(cell != -1):
        shortestPath.appendleft(cell)           # inserts cell at the beginning of deque
        cell = pred[cell]
    for cell in shortestPath:                   # draw shortest path 
        blue.goto(cell)
        blue.stamp() 


#  initialise lists
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
walls = []
path = []
visited = set()                 # A hash table for search and insert cell in O(1) complexity 
queue = []                      
pred = {}
dy = [24,0,-24,0]               #navigate between child of cell
dx = [0,24,0,-24]
found = 0
setup_maze(grid1)                    # call setup maze function
dfs(start_x, start_y)                # call DFS function
found = 0 
visited.clear()                     #clear visited to use it in next function
BFS(start_x,start_y)                #BFS to find shortest path 

wn.exitonclick()                        # exit out Pygame when x is clicked
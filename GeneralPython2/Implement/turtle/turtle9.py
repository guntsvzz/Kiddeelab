import turtle  
  
# Creating a method for the moving of an object  
def move_obj(ball):  
    # filling the color in the ball  
    ball.fillcolor('yellow')  
    # starting to color the ball  
    ball.begin_fill()  
    # drawing the circle  
    ball.circle(25)  
    # ending the color filling in the ball  
    ball.end_fill()  
  
# Main Code  
if __name__ == "__main__":  
  
    # Creating a screen object  
    scr = turtle.Screen()  
    # setting the screen size  
    scr.setup(650, 650)  
    # setting the screen background color  
    scr.bgcolor('light green')  
    # screen updation   
    scr.tracer(0)  
    # creating a turtle object  
    ball = turtle.Turtle()  
    # setting the turtle object color to red  
    ball.color('red')  
    # setting the turtle object speed  
    ball.speed(0)  
    # setting the turtle object width  
    ball.width(2)  
    # hiding the turtle object  
    ball.hideturtle()  
    # turtle object in air  
    ball.penup()  
    # setting the initial position  
    ball.goto(-350, 0) 
    # moving turtle object to the surface  
    ball.pendown()  
  
    # running infinite loop  
    while True:  
        # clearing the turtle work  
        ball.clear()  
        # calling the method to draw the ball  
        move_obj(ball)  
        # updating the screen  
        scr.update()  
        # forward motion by turtle object  
        ball.forward(0.2)  
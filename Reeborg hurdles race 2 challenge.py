#Hurdles race 2

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()

    
while not at_goal():
    move()
    jump()
    turn_left()
        

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

for step in range(6):
    move()
    jump()
    turn_left()
        

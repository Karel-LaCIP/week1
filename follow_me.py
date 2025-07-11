from graphics import Canvas
import time

CANVAS_SIZE = 400
BALL_DIAMETER = 50
BALL_RADIUS = BALL_DIAMETER // 2
PAUSE_TIME = 1/50

def main():
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
    ball = canvas.create_oval(
        0, 0,
        BALL_DIAMETER, 
        BALL_DIAMETER,
        'blue'
    )
    
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()

        if mouse_x >= BALL_RADIUS and mouse_x <= CANVAS_SIZE - BALL_RADIUS and mouse_y >= BALL_RADIUS and mouse_y <= CANVAS_SIZE - BALL_RADIUS:    
            canvas.moveto(ball, mouse_x - BALL_RADIUS, mouse_y - BALL_RADIUS)
        
        time.sleep(PAUSE_TIME)
        print("Mouse location: (" + str(mouse_x) + ", " + str(mouse_y) + ")")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()




"""Another version of the code:
from graphics import Canvas
import time

CANVAS_SIZE = 400
BALL_DIAMETER = 50
PAUSE_TIME = 1/50

def main():
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
    ball = canvas.create_oval(
        0, 0,
        BALL_DIAMETER, 
        BALL_DIAMETER,
        'blue'
    )
    
    
    while True:
        radius=BALL_DIAMETER/2
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()

        constrained_x = min(max(mouse_x, BALL_DIAMETER/2), CANVAS_SIZE - BALL_DIAMETER/2)
        constrained_y = min(max(mouse_y, BALL_DIAMETER/2), CANVAS_SIZE - BALL_DIAMETER/2)
        
        canvas.moveto(ball, constrained_x-BALL_DIAMETER/2, constrained_y-BALL_DIAMETER/2)
        
        time.sleep(PAUSE_TIME)
        print("Mouse location: (" + str(mouse_x) + ", " + str(mouse_y) + ")")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()"""

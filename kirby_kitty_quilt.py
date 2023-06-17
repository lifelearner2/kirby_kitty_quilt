from graphics import Canvas
import time

# each patch is a square with this width and height:
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2
DELAY = 0.05


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # draw the first row of patches
    draw_square_patch(canvas, 0, 0) 
    time.sleep(DELAY)
    #the second and third arguments above are the start_x and start_y coordinates
    draw_circle_patch(canvas, PATCH_SIZE, 0)
    time.sleep(DELAY)
    draw_square_patch(canvas, PATCH_SIZE*2, 0)
    time.sleep(DELAY)
    draw_circle_patch(canvas, PATCH_SIZE*3, 0)
    time.sleep(DELAY)
    # TODO: your code here
    draw_second_row_square(canvas,PATCH_SIZE, PATCH_SIZE)
    draw_second_row_square(canvas,PATCH_SIZE*3, PATCH_SIZE)
    draw_second_row_circle(canvas,PATCH_SIZE*0, PATCH_SIZE)
    draw_second_row_circle(canvas,PATCH_SIZE*2, PATCH_SIZE) 
    time.sleep(DELAY)
 
    
def draw_circle_patch(canvas, start_x, start_y):
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    canvas.create_oval(start_x, start_y, end_x, end_y, 'salmon')
    print(start_x, start_y)
    draw_hello_kitty(canvas, start_x, start_y)
    time.sleep(DELAY)
    draw_hello_whiskers(canvas, start_x, start_y)
    draw_hello_ears(canvas, start_x, start_y)
    draw_hello_bow(canvas, start_x, start_y)
    
    
def draw_square_patch(canvas, start_x, start_y):
    # draws a purple frame at (start_x, start_y)
    end_x = start_x + PATCH_SIZE
    #values for start_x & start_y are coming from the values being passed in the main function
    end_y = start_y + PATCH_SIZE
    inset = 20
    # first draw a purple square over the entire patch
    canvas.create_rectangle(start_x, start_y, end_x, end_y, 'purple')
    # then draw a smaller white square on top
    canvas.create_rectangle(start_x+inset, start_y+inset, 
        end_x-inset, end_y-inset, 'white')
    draw_kirby(canvas, start_x, start_y)
    time.sleep(DELAY)
  
  
def draw_kirby(canvas, start_x, start_y):
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 20
    canvas.create_oval(start_x+inset, start_y+inset, end_x-inset, end_y-inset, 'pink')
    draw_kirby_left_eye(canvas, start_x, start_y)
    draw_kirby_right_eye(canvas, start_x, start_y)
    time.sleep(DELAY)
    draw_kirby_left_middle_eye(canvas, start_x, start_y)
    time.sleep(DELAY)
    draw_kirby_right_middle_eye(canvas, start_x, start_y)
    draw_kirby_mouth_outline(canvas, start_x, start_y)
    # draw_kirby_right_arm(canvas, start_x, start_y)

def draw_kirby_left_eye(canvas, start_x, start_y):
    draw_kirby_left_eye_outline(canvas, start_x, start_y)
    # custom_color = (0, 128, 255)  # In-between blue and cyan
    # custom_color = "#0080FF"  # In-between blue and cyan
    inset_x = 35
    inset_y = 30
    eye_width = 10
    eye_height = 24
    canvas.create_oval(start_x + inset_x, start_y + inset_y,
                       start_x + inset_x + eye_width, start_y + inset_y + eye_height, 'blue')
    time.sleep(DELAY)
                       
def draw_kirby_left_eye_outline(canvas, start_x, start_y):
    inset_x = 33
    inset_y = 28
    eye_width = 14
    eye_height = 28
    canvas.create_oval(start_x + inset_x, start_y + inset_y,
                       start_x + inset_x + eye_width, start_y + inset_y + eye_height, 'black')
    time.sleep(DELAY)
                       
def draw_kirby_left_middle_eye(canvas, start_x, start_y):
    inset_x = 36
    inset_y = 30
    eye_width = 8
    eye_height = 14
    canvas.create_oval(start_x + inset_x, start_y + inset_y,
                       start_x + inset_x + eye_width, start_y + inset_y + eye_height, 'white')
    time.sleep(DELAY)
                       
def draw_kirby_right_eye_outline(canvas, start_x, start_y):
    inset_x = 53
    inset_y = 28
    eye_width = 14
    eye_height = 28
    canvas.create_oval(start_x + inset_x, start_y + inset_y,
                       start_x + inset_x + eye_width, start_y + inset_y + eye_height, 'black')
    time.sleep(DELAY)
                       
def draw_kirby_right_eye(canvas, start_x, start_y):
    # custom_color = "#0080FF"  # In-between blue and cyan
    draw_kirby_right_eye_outline(canvas, start_x, start_y)
    # custom_color = (0, 128, 255)  # In-between blue and cyan
    inset_x = 55
    inset_y = 30
    eye_width = 10
    eye_height = 24
    canvas.create_oval(start_x + inset_x, start_y + inset_y,
                       start_x + inset_x + eye_width, start_y + inset_y + eye_height, 'blue')
    
    # canvas.create_rectangle(5, 50, 100, 200, custom_color)
                       
def draw_kirby_right_middle_eye(canvas, start_x, start_y):
    inset_x = 56
    inset_y = 30
    eye_width = 8
    eye_height = 14
    canvas.create_oval(start_x + inset_x, start_y + inset_y,
                       start_x + inset_x + eye_width, start_y + inset_y + eye_height, 'white')
    time.sleep(DELAY)                       

def draw_kirby_mouth_outline(canvas, start_x, start_y):
    inset_x = 42
    inset_y = 57
    mouth_width = 8
    mouth_height = 7
    canvas.create_line(start_x + inset_x, start_y + inset_y, start_x + inset_x + mouth_width, start_y + inset_y + mouth_height, 'black')
    time.sleep(DELAY)    
    canvas.create_line(start_x + inset_x +20, start_y + inset_y +1, start_x + inset_x + mouth_width, start_y + inset_y + mouth_height, 'black')
    canvas.create_line(start_x + inset_x +18, start_y + inset_y, start_x + inset_x + mouth_width -10, start_y + inset_y + mouth_height -8, 'black')
    
def draw_kirby_right_arm(canvas, start_x, start_y):
    # custom_color = "#0080FF"  # In-between blue and cyan
    draw_kirby_right_arm(canvas, start_x, start_y)
    # custom_color = (0, 128, 255)  # In-between blue and cyan
    inset_x = 38
    inset_y = 10
    arm_width = 10
    arm_height = 24
    canvas.create_oval(start_x + inset_x +1, start_y + inset_y+1,
                       start_x + inset_x + arm_width + 1, start_y + inset_y + arm_height +1, 'orange')

def draw_hello_outline(canvas, start_x, start_y):
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 11
    canvas.create_oval(start_x+inset, start_y+inset, end_x-inset, end_y-inset, 'black')
    time.sleep(DELAY)
    
def draw_hello_kitty(canvas, start_x, start_y):  
    draw_hello_outline(canvas, start_x, start_y)
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 13
    canvas.create_oval(start_x+inset, start_y+inset, end_x-inset, end_y-inset, 'white')
    draw_hello_left_eye(canvas, start_x, start_y)
    draw_hello_right_eye(canvas, start_x, start_y)
    draw_hello_nose(canvas, start_x, start_y)
    time.sleep(DELAY)
  

    
def draw_hello_left_eye(canvas, start_x, start_y):
    inset_x = 62
    inset_y = 50
    eye_width = 10
    eye_height = 12
    canvas.create_oval(start_x + inset_x, start_y + inset_y,
                       start_x + inset_x + eye_width, start_y + inset_y + eye_height, 'black')
    time.sleep(DELAY)

def draw_hello_right_eye(canvas, start_x, start_y):
    inset_x = 26
    inset_y = 50
    eye_width = 10
    eye_height = 12
    canvas.create_oval(start_x + inset_x, start_y + inset_y,
                       start_x + inset_x + eye_width, start_y + inset_y + eye_height, 'black')
    time.sleep(DELAY)
                       
def draw_hello_nose(canvas, start_x, start_y):
    draw_hello_nose_outline(canvas, start_x, start_y)
    inset_x = 45
    inset_y = 62
    nose_width = 7
    nose_height = 5
    canvas.create_oval(start_x + inset_x, start_y + inset_y, start_x + inset_x + nose_width, start_y + inset_y + nose_height, 'orange')
    time.sleep(DELAY)
    
 
def draw_hello_nose_outline(canvas, start_x, start_y):
    inset_x = 44
    inset_y = 61
    nose_width = 9
    nose_height = 7
    canvas.create_oval(start_x + inset_x, start_y + inset_y, start_x + inset_x + nose_width, start_y + inset_y + nose_height, 'black')
    time.sleep(DELAY)
    
def draw_hello_whiskers(canvas, start_x, start_y):
    # Left whiskers
    whisker_start_x = start_x + 32
    whisker_start_y = start_y + 65

    canvas.create_line(whisker_start_x, whisker_start_y, whisker_start_x - 20, whisker_start_y - 10, 'black')
    canvas.create_line(whisker_start_x, whisker_start_y, whisker_start_x - 20, whisker_start_y, 'black')
    canvas.create_line(whisker_start_x, whisker_start_y, whisker_start_x - 20, whisker_start_y + 10, 'black')

    # Right whiskers
    whisker_start_x = start_x + 68
    whisker_start_y = start_y + 65

    canvas.create_line(whisker_start_x, whisker_start_y, whisker_start_x + 20, whisker_start_y - 10, 'black')
    canvas.create_line(whisker_start_x, whisker_start_y, whisker_start_x + 20, whisker_start_y, 'black')
    canvas.create_line(whisker_start_x, whisker_start_y, whisker_start_x + 20, whisker_start_y + 10, 'black')

def draw_hello_ears(canvas, start_x, start_y):
    # Left ear
    canvas.create_line(start_x + 25, start_y + 20, start_x + 35, start_y + 5, 'white')
    canvas.create_line(start_x + 35, start_y + 5, start_x + 45, start_y + 20, 'white')
    canvas.create_line(start_x + 25, start_y + 20, start_x + 45, start_y + 20, 'white')

    # Right ear
    canvas.create_line(start_x + 55, start_y + 20, start_x + 65, start_y + 5, 'white')
    canvas.create_line(start_x + 65, start_y + 5, start_x + 75, start_y + 20, 'white')
    canvas.create_line(start_x + 55, start_y + 20, start_x + 75, start_y + 20, 'white')

def draw_hello_bow(canvas, start_x, start_y):
    #center circle
    canvas.create_oval(start_x + 55, start_y + 10, start_x + 78, start_y + 30, 'red')
    
    #left triangle
    canvas.create_line(start_x + 65, start_y + 16, start_x + 50, start_y + 24, 'red')
    canvas.create_line(start_x + 70, start_y + 36, start_x + 50, start_y + 24, 'red')
    #right triangle
    canvas.create_line(start_x + 80, start_y + 26, start_x + 70, start_y + 34, 'red')
    
def draw_second_row_square(canvas, start_x, start_y):
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 20
    canvas.create_rectangle(start_x, start_y, end_x, end_y, 'purple')
    canvas.create_rectangle(start_x+inset, start_y+inset, 
        end_x-inset, end_y-inset, 'white')   
    draw_kirby(canvas, start_x, start_y)
    time.sleep(DELAY)
  

def draw_second_row_circle(canvas, start_x, start_y):        
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    canvas.create_oval(start_x, start_y, end_x, end_y, 'salmon')
    draw_hello_kitty(canvas, start_x, start_y)
    time.sleep(DELAY)
    draw_hello_whiskers(canvas, start_x, start_y)
    draw_hello_ears(canvas, start_x, start_y)
    draw_hello_bow(canvas, start_x, start_y)
  
    print(start_x, start_y)



if __name__ == '__main__':
    main()
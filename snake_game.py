from tkinter import Tk, Label, Canvas
import random


GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BACKGROUND_COLOR = '#000000'
last_direction = 'down'


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.square = []
        
        for i in range(0, BODY_PARTS):
            self.coordinates.append ([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = 'snake')
            self.square.append(square)
    

class Food:

    def __init__(self):
        x = random.randint(0, (GAME_WIDTH//SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT//SPACE_SIZE)-1) * SPACE_SIZE
        self.coordinates = [x,y]
        self.food_item = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR,  tag = 'FOOD')


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction =='up':
        y-= SPACE_SIZE

    elif direction =='down':
        y+= SPACE_SIZE

    elif direction =='left':
        x-= SPACE_SIZE
    elif direction =='right':
        x+= SPACE_SIZE

    snake.coordinates.insert(0,[x,y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill= SNAKE_COLOR, tag = 'snake')
    snake.square.insert(0, square)

    if x == food.coordinates[0] and y== food.coordinates[1]:

        global score

        score +=1

        label.config(text = 'Score:{}'.format(score))

        canvas.delete('FOOD')

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.square[-1])

        del snake.square[-1] 

    if check_collisions(snake, food):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def check_collisions(snake, food):
    head_coords = snake.coordinates[0]

    if(
        head_coords[0]< 0 or
        head_coords[1]< 0 or
        head_coords[0] >= GAME_WIDTH or
        head_coords[1] >= GAME_HEIGHT
    ):
        game_over()


    for segment in snake.coordinates[1:]:
        if head_coords == segment:
            game_over


    if head_coords == food.coordinates:
        snake.body_size += 1
        canvas.delete('FOOD')
        food = Food()
        update_score()

def update_score():
    global score
    score += 1
    label.config(text='Score:{}'.format(score))

def game_over():
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2, text = 'Game Over', font=('consolas', 40), fill= 'white')
    window.quit()

    
def change_direction(new_direction):
    global direction, last_direction
    if (
        (new_direction == 'left' and last_direction != 'right') or
        (new_direction == 'right' and last_direction != 'left') or
        (new_direction == 'up' and last_direction != 'down') or
        (new_direction == 'down' and last_direction != 'up')
    ):
        direction = new_direction
        last_direction = new_direction




window = Tk()
window.title('Snake game')
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text='Score:{}'.format(score), font=('consolas', 40), fg= 'white', bg= 'black')
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


x= (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)

window.geometry(f'{int(window_width)}x{int(window_height)}+{int(x)}+{int(y)}')

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
import turtle
import time
import random

delay = 0.15

screen = turtle.Screen()
screen.title('Hungry Snek')
screen.bgcolor('blue')
screen.setup(width=600, height=600)
screen.tracer(0)

snek = turtle.Turtle()
snek.speed(0)
snek.shape('square')
snek.color('black')
snek.penup()
snek.goto(0,0)
snek.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

bodys = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.goto(0, 200)
pen.write('Score: 0 High Score: 0', align='center', font=('Courier', 24, 'normal'))
pen.hideturtle()

def go_up():
    if snek.direction != 'down':
        snek.direction = 'up'

def go_down():
    if snek.direction != 'up':
        snek.direction = 'down'

def go_left():
    if snek.direction != 'right':
        snek.direction = 'left'

def go_right():
    if snek.direction != 'left':
        snek.direction = 'right'
    
def move():
    if snek.direction == 'up':
        y = snek.ycor()
        snek.sety(y+20)
    if snek.direction == 'down':
        y = snek.ycor()
        snek.sety(y-20)
    if snek.direction == 'left':
        x = snek.xcor()
        snek.setx(x-20)
    if snek.direction == 'right':
        x = snek.xcor()
        snek.setx(x+20)

screen.listen()
screen.onkeypress(go_up, 'w')
screen.onkeypress(go_down, 's')
screen.onkeypress(go_left, 'a')
screen.onkeypress(go_right, 'd')

while True:
    screen.update()
    
    if snek.xcor()>290 or snek.xcor()<-290 or snek.ycor()>290 or snek.ycor()<-290:
        time.sleep(1)
        snek.goto(0,0)
        snek.direction = 'stop'
        
        for body in bodys:
            body.goto(1000,1000)
        
        bodys.clear()
    
    if snek.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)
        
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape('square')
        new_body.color('green')
        new_body.penup()
        bodys.append(new_body)
        
    for index in range(len(bodys)-1, 0, -1):
        x = bodys[index-1].xcor()
        y = bodys[index-1].ycor()
        bodys[index].goto(x, y)
    
    if len(bodys) > 0:
        x = snek.xcor()
        y = snek.ycor()
        bodys[0].goto(x, y)
        
    move()
    
    for body in bodys:
        if body.distance(snek) < 20:
            time.sleep(1)
            snek.goto(0, 0)
            snek.direction = 'stop'
            
            for body in bodys:
                body.goto(1000, 1000)
                
            bodys.clear()
    
    time.sleep(delay)
    
screen.mainloop()
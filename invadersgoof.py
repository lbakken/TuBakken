import turtle
import time
import random

delay = .04

screen = turtle.Screen()
screen.title('Oh No Invader!!?')
screen.bgcolor('black')
screen.setup(600, 600)
screen.tracer(0)

dude = turtle.Turtle()
dude.speed(0)
dude.shape('triangle')
dude.color('white')
dude.penup()
dude.goto(0, -250)
dude.direction = 'stop'
dude.setheading(90)

shot = turtle.Turtle()
shot.speed(0)
shot.penup()
shot.shape('arrow')
shot.color('red')
shot.setheading(90)
shot.shapesize(.5, .5)
shot.direction = 'stop'
shot.hideturtle()
shotspeed = 20

shotstate = 'ready'

more_enemies = 12
enemies = []
for i in range(more_enemies):
    enemies.append(turtle.Turtle())
    
for enemy in enemies:
    enemy.speed(0)
    enemy.shape('turtle')
    enemy.color('green')
    enemy.penup()
    enemy.setheading(270)
    enemy.direcion = 'stop'
    x = random.randint(-200, 200)
    y = random.randint(100, 200)
    enemy.goto(x, y)

enemyspeed = 5

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.goto(0, 200)
pen.write('Score: {}  High Score: {}', align='center', font=('Courier', 24, 'normal'))
pen.hideturtle()

def go_left():
    dude.direction = 'left'

def go_right():
    dude.direction = 'right'
    
def pls_stop():
    dude.direction = 'stop'
    
def pew_pew():
    shot.direction = 'up'
    
def no_pew():
    shot.direction = 'go'
    
def shoot_shot():
    global shotstate
    if shotstate == 'ready':
        shotstate = 'fire'
        x = dude.xcor()
        y = dude.ycor()
        shot.setposition(x, y+15)
        shot.showturtle()

def move():
    if dude.direction == 'left':
        x = dude.xcor()
        dude.setx(x-10)
    if dude.direction == 'right':
        x = dude.xcor()
        dude.setx(x+10)
    if dude.direction == 'stop':
        x = dude.xcor()
        dude.setx(x)

screen.listen()
screen.onkeypress(go_left, 'a')
screen.onkeypress(go_right, 'd')
screen.onkeyrelease(pls_stop, 'a')
screen.onkeyrelease(pls_stop, 'd')
screen.onkeypress(shoot_shot, 'space')

while True:
    screen.update()
    
    for enemy in enemies:        
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
    
        if enemy.xcor() > 280:
            enemyspeed *= -1
            enemy.sety(enemy.ycor()-40)
        
        if enemy.xcor() < -280:
            enemyspeed *= -1
            enemy.sety(enemy.ycor()-40)
            
        if shot.distance(enemy) < 30:
            
            shot.hideturtle()
            shotstate= 'ready'
        
        if enemy.distance(dude) < 30:
            dude.hideturtle
            enemy.hideturtle
            print ('Game Over')
            break 
    
    if dude.xcor() > 280 or dude.xcor() < -280:
        dude.direction = 'stop'
        if dude.xcor() > 280:
            dude.goto(279, -250)
        if dude.xcor() < -280:
            dude.goto(-279, -250)
    
    if shot.ycor() > 280:
        shot.hideturtle()
        shotstate = 'ready' 
        
    if shotstate == 'fire':
        y = shot.ycor()
        y += shotspeed
        shot.sety(y)
    
    move()
    
    time.sleep(delay)

screen.mainloop()
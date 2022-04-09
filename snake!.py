import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("brown")
food.penup()
x = random.randint(-290,290)
y = random.randint(-240,290)
food.goto(x,y)

poison = turtle.Turtle()
poison.speed(0)
poison.shape("circle")
poison.color("green")
poison.penup()
x = random.randint(-290,290)
y = random.randint(-240,290)
food.goto(x,y)

deadly = turtle.Turtle()
deadly.speed(0)
deadly.shape("circle")
deadly.color("green")
deadly.penup()
x = random.randint(-290,290)
y = random.randint(-240,290)
food.goto(x,y)

no_touch = turtle.Turtle()
no_touch.speed(0)
no_touch.shape("circle")
no_touch.color("green")
no_touch.penup()
x = random.randint(-290,290)
y = random.randint(-240,290)
food.goto(x,y)


segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Terminal", 20, "normal"))

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"




def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_down, "Down")


while True:
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-256:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0
            
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Terminal", 20, "normal"))
            
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-240,290)
        food.goto(x,y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score += 10

        if score >= 100:
            score += random.randint(10,100)

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Terminal", 20, "normal"))


    if head.distance(poison) < 20:
        x = random.randint(-290,290)
        y = random.randint(-240,290)
        poison.goto(x,y)   
        score -= 10
        if score >=100:
            score -= random.randint(50,100)
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Terminal", 20, "normal"))

    if head.distance(deadly) < 20:
        x = random.randint(-290,290)
        y = random.randint(-240,290)
        deadly.goto(x,y)   
        score -= 10
        if score >=100:
            score -= random.randint(50,100)
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Terminal", 20, "normal"))

    if head.distance(no_touch) < 20:
        x = random.randint(-290,290)
        y = random.randint(-240,290)
        no_touch.goto(x,y)   
        score -= 10
        if score >=100:
            score -= random.randint(50,100)
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Terminal", 20, "normal"))


    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    
    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)

            

            
            segments.clear()


            score = 0
            
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Terminal", 20, "normal"))

    if score == -10:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0
            
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Terminal", 20, "normal"))
            

            

    time.sleep(delay)
    






wn.mainloop()
#pong game in python

import turtle  #modul i thjeshte per krijuar lojra

ek = turtle.Screen()
ek.title("pong game")
ek.bgcolor("black")
ek.setup(width = 800, height = 600)  #permasat e ekranit
ek.tracer(0)  #ndalon updaten e ekranit dhe shpejton lojen

#score
score_a = 0
score_b = 0


#padle a

padle_a = turtle.Turtle() #krijon nje objekt me emrin padle_a nga klasa Turtle()
padle_a.speed(0) #shpejtesia me e madhe e mundshme e animimit
padle_a.shape("square")
padle_a.shapesize(stretch_wid=5, stretch_len=1)

padle_a.color("white")
padle_a.penup() #nuk le nje vije kur leviz, sepse objektet ne kete modul lene vija nga pas kur levizin
padle_a.goto(-350, 0)#ne cilat koordinata mund te levizi

#padle b

padle_b = turtle.Turtle() #krijon nje objekt me emrin padle_a nga klasa Turtle()
padle_b.speed(0) #shpejtesia me e madhe e mundshme e animimit
padle_b.shape("square")
padle_b.shapesize(stretch_wid=5, stretch_len=1)

padle_b.color("white")
padle_b.penup() #nuk le nje vije kur leviz, sepse objektet ne kete modul lene vija nga pas kur levizin
padle_b.goto(+350, 0)#ne cilat koordinata mund te levizi


#ball
ball = turtle.Turtle() #krijon nje objekt me emrin padle_a nga klasa Turtle()
ball.speed(0) #shpejtesia me e madhe e mundshme e animimit
ball.shape("square")


ball.color("white")
ball.penup() #nuk le nje vije kur leviz, sepse objektet ne kete modul lene vija nga pas kur levizin
ball.goto(0, 0)#ne cilat koordinata mund te levizi
ball.dx = 0.4
ball.dy = 0.4 #me sa pixel leviz topi ne boshte

#pen. sherben per te mbajtur piket
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #e fshehim objektin sepse nuk kemi pse ta shikojme
pen.goto(0, 250)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#funksionet

def padle_A_up():
    y = padle_a.ycor() #merr koordinatat e y
    y += 20
    padle_a.sety(y) #update koordinaten y

def padle_A_down():
    y = padle_a.ycor() #merr koordinatat e y
    y -= 20
    padle_a.sety(y) #update koordinaten y



def padle_B_up():
    y = padle_b.ycor() #merr koordinatat e y
    y += 20
    padle_b.sety(y) #update koordinaten y

def padle_B_down():
    y = padle_b.ycor() #merr koordinatat e y
    y -= 20
    padle_b.sety(y) #update koordinaten y



ek.listen()
ek.onkeypress(padle_A_up, "w") 
ek.onkeypress(padle_A_down, "s")

ek.onkeypress(padle_B_up, "Up") 
ek.onkeypress(padle_B_down, "Down") 






while True:
    ek.update()

    #levizja e topit
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy)

    #border 
    if ball.ycor() > 290:  #kontrollon nese topi arrin kufirin siper dhe nese arrin e kthen ne drejtim te kundert. 290 sepse boshtet jane 300 me 300 dhe topi eshte 20 me 20
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:  #kontrollon nese topi arrin kufirin poshte dhe nese arrin e kthen ne drejtim te kundert
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: #kur topi kalon krahun e majte ose te djathe nis perseri nga qendra dhe quhet pike
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()   #update piket pas cdo raundi
        pen.write("Player A: {}  Player B: {} ".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1  
        score_b += 1
        pen.clear()  #update piket pas cdo raundi
        pen.write("Player A: {}  Player B: {} ".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            

    #padle and ball collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < padle_a.ycor() + 40 and ball.ycor() > padle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1   

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < padle_b.ycor() + 40 and ball.ycor() > padle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1            
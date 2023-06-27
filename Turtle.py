import turtle

# Ustawienie tła na zielone
turtle.bgcolor("green")

# Ustawienie długości i koloru pióra
turtle.pensize(3)
turtle.pencolor("red")
turtle.fillcolor("red")

# Przejście do środka ekranu
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Narysowanie kształtu serca
turtle.begin_fill()
turtle.left(45)
turtle.forward(150)
turtle.circle(75, 180)
turtle.right(90)
turtle.circle(75, 180)
turtle.forward(150)
turtle.end_fill()

# Ukrycie żółwia i wyświetlenie wyniku
turtle.hideturtle()
turtle.done()

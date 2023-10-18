import turtle as turtle
import random

print("Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, go to the result tab!")

turtle.penup()
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(300)
turtle.pendown()

turtle.write("Drawing App!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()

turtle.write("To draw a shape, go to the Console tab and choose an option!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.pendown()

def star():
  # Star
  for i in range(0,5):
    turtle.forward(110)
    turtle.left(216)

def square():
  # Square
  for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)

def hexagon():
  # Hexagon
  for i in range(0,6):
    turtle.forward(100)
    turtle.right(60)

def triangle():
  # Triangle
  for i in range(0,3):
    turtle.forward(100)
    turtle.right(120)

def circle():
  # Circle
  turtle.circle(60)

def pentagon():
  # Pentagon
  for i in range(0,5):
    turtle.forward(100)
    turtle.right(72)

def octagon():
  # Octagon
  for i in range(0,8):
    turtle.forward(80)
    turtle.right(45)

def rectangle():
  # Rectangle
  for i in range(0,2):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)

selection = input(
  "1. Star\n2. Square\n3. Hexagon\n4. Triangle\n5. Circle\n6. Pentagon\n7. Octagon\n8. Rectangle\nSelect a number: ")
if selection == "1":
  print("Excellent choice! Go to the result tab to see your creation.")
  star()
elif selection == "2":
  print("Excellent choice! Go to the result tab to see your creation.")
  square()
elif selection == "3":
  print("Excellent choice! Go to the result tab to see your creation.")
  hexagon()
elif selection == "4":
  print("Excellent choice! Go to the result tab to see your creation.")
  triangle()
elif selection == "5":
  print("Excellent choice! Go to the result tab to see your creation.")
  circle()
elif selection == "6":
  print("Excellent choice! Go to the result tab to see your creation.")
  pentagon()
elif selection == "7":
  print("Excellent choice! Go to the result tab to see your creation.")
  octagon()
elif selection == "8":
  print("Excellent choice! Go to the result tab to see your creation.")
  rectangle()
import turtle as turtle

def star():
    #use for loop to draw star
    for i in range(5):
        turtle.pencolor("black")
        turtle.forward(110)
        turtle.left(216)

def square():
    #use for loop to draw square
    for i in range(4):
        turtle.pencolor("purple")
        turtle.forward(100)
        turtle.right(90)

def hexagon():
    #use for loop to draw hexagon
    for i in range(6):
        turtle.pencolor("green")
        turtle.forward(100)
        turtle.right(60)

selection = input("1. Star\n2. Square\n3. Hexagon\nSelect a number: ")
if selection == "1":
  print("Excellent choice! Go to the result tab to see your creation.")
  star()
elif selection == "2":
  print("Excellent choice! Go to the result tab to see your creation.")
  square()
elif selection == "3":
  print("Excellent choice! Go to the result tab to see your creation.")
  hexagon()
import turtle as turtle
import datetime 

turtle.pencolor("orange")
turtle.forward(100)
turtle.right(60)

turtle.pencolor("red")
turtle.forward(100)
turtle.right(60)

turtle.pencolor("yellow")
turtle.forward(100)
turtle.right(60)

turtle.pencolor("orange")
turtle.forward(100)
turtle.right(60)

turtle.pencolor("red")
turtle.forward(100)
turtle.right(60)

turtle.pencolor("yellow")
turtle.forward(100)
turtle.right(60)

#Get the current time
current_time = datetime.datetime.now()

#Print the date in 00/00/00 format
print("Date (MM/DD/YY):", current_time.strftime("%m/%d/%y"))

#Print the date in January, 1, 2025 format
print("Date (Month, Day, Year):", current_time.strftime("%B, %d, %Y"))

#Print the date with the current time
print("Date and Time:", current_time)
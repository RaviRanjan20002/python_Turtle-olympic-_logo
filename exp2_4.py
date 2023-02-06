'''    * we can make more than one turtle
 for moving the turtle we have below function
     t1.forward(distance) for moving or drawing a line in forward t1 turtle in forward direction
     t1.backward(distance) for moving or draw aline in backward dirn t1 turtle in backward direction
      or t1.fd(distance),t1.bd(distance)
   eg  t1.forward(20)
 
 for x and y both cordinate we have one function
   t1.goto(x,y)
   eg. t1.goto(100,100)

 for giving a direction we have some function
     t1.left(angle)   or t1.lt(angle)
     t1.right(angle)  ot t1.rt(angle)
  eg t1.left(30)

 to bring back(original position) turtle after movement is we have one function
  t1.home();
 
 for Drawing shape in turtle
  for circle 
  t1.circle(radius)
  for Dot
  t1.dot(diameter)
  for Rectangle
  t1.forward(100)
  t1.left(90)
  t1.fd(50)
  t1.left(90)
  t1.fd(100)
  t1.left(90)
  t1.fd(50)

  from goto function
 t1.goto(100,0)
 t1.goto(100,50)
 t1.goto(0 ,50)
 t1.goto(0,0)

// for traingle
 
 t1.goto(100,0)
 t1.goto(0,100)
 t1.goto(100,0)
 t1.goto(0,0)

 for hiding turtle
 turtle.hideturtle()  or ht() //hideturtle is a function
 for showing turtle
 turtle.showturtle()  or st()
 // to show turtle after draw
  t1.goto(100,0)
  t1.st()

 for using pen we have function
 penup() // it is used for nothing to draw 
 and after sometime if you want to deraw something then use given below function 
 pendown() //to draw something
 
 
 for increasing thickness of pen we have some function
 t1.pensize(thickness)
 
 for giving color to pen we have function
 t1.pencolor("red")
 
 
 how to set title in screen
 
 s=turtle.getscreen()
 s.title("Ravi Ranjan") // it will call through screen object
 
 how to change turtle shape
 t1.shape("arrow")  // arrow,square,classic,turtle,circle,triangle
 
 how to change shape and size of turtle
 t1.shapesize(stretch length,stretch width,outline width)
 
 // how to use loop
 for angle in range(0,901,90):
     t1.left(angle)
 
 filling color in various shape

 t1.fillcolor("red")
 t1.begin_fill()
 // draw any closed shape diagram
 t1.end_fill()

 eg
  t1.fillcolor("red")
  t1.begin_fill()
  t1.circle(50)  // draw any closed shape diagram
  t1.end_fill()
  
   TURTLE stamp
   it is used to create copy of turtle
   t1.stamp()
   
   eg
   for e in range(10)
   x=t1.stamp() //in x there is stamp id which help in removing stamp
   t1.fd(100)
   t1.lt(60)
   t1.clearstamp(x) // to remove stamp we use this function where x is id

 t1.clearstamps() // it delete all stamp
 t1.clearstamps(5) // it delete first 5 stamp
 t1.clearstamps(-5) // it delete last 5 stamp
 

 undo turtle actions
 t1.undo() // it will undo the action of turtle

 t1.undobuffer.bufsize // to know the count for undo action
 t1.setundobuffer(size)   //to set the count of undo action but if you want to set
 the size then u must set it in starting of your program because after setting this
 undobufferenteries became zero

 t1.undobufferentries() // to know the count of current undo action



 reset and clear turtle drawings
 t1.reset() // all drawing will be erased and turtle will be come back at original position
 t1.clear()  // all drawing will be erased but turtle will not come back at original position

 '''

import turtle
s=turtle.getscreen()
t1=turtle.Turtle()
t1.ht()
#here Turtle is class and we make a object and store reference in 
t1.pencolor("blue")
t1.pensize(10)
t1.circle(60)
t2=turtle.Turtle()
t2.ht()
t2.penup()
t2.fd(140)
t2.pendown()
t2.pencolor("black")
t2.pensize(10)
t2.circle(60)
t3=turtle.Turtle()
t3.ht()
t3.penup()
t3.fd(280)
t3.pendown()
t3.pencolor("red")
t3.pensize(10)
t3.circle(60)


t1.right(90)
t1.pencolor("yellow")
t1.circle(60)

t2.right(90)
t2.pencolor("green")
t2.circle(60)

t1.clearstamps()
t2.clearstamps()
t3.clearstamps()

turtle.exitonclick()

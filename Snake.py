from casioplot import *
from random import *
from turtle import *

vie = 6
heartP = 6

def heart(x):
  posx = [x,x,x,x,x,x,x-1,x-1,x-1,x-1,x-1,x-1,x-2,x-2,x-3,x-3,x-4,x-4,x-5,x-5,x-6,x-6,x-7,x-7,x-8,x-8,x-9,x-9,x-10,x-10,x-11,x-11,x-12,x-12,x-13,x-13,x-14,x-14,x-14,x-14,x-14,x-14,x-15,x-15,x-15,x-15,x-15,
  x-15,x-13,x-13,x-12,x-12,x-11,x-11,x-10,x-10,x-9,x-9,x-8,x-8,x-7,x-7,x-6,x-6,x-5,x-5,x-4,x-4,x-3,x-3,x-2,x-2]
  posy = [7,8,9,10,11,12,7,8,9,10,11,12,13,14,13,14,15,16,15,16,17,18,17,18,17,18,17,18,15,16,15,16,13,14,13,14,7,8,9,10,11,12,7,8,9,10,11,12,5,6,5,6,5,6,5,6,7,8,7,8,7,8,7,8,5,6,5,6,5,6,5,6]
  l = 0
  while l < 72:
    set_pixel(posx[l],posy[l])
    l = l + 1

def affheart(vie):
  a = 0
  x = 374
  while a < vie / 2:
     heart(x)
     x = x - 18
     a = a + 1

def fillheart1(x):
  xh = [x,x,x,x,x,x,x-1,x-1,x-1,x-1,x-1,x-1,x-2,x-2,x-2,x-2,x-2,x-2,x-2,x-2,x-3,x-3,x-3,x-3,x-3,x-3,x-3,x-3,x-4,x-4,x-4,x-4,x-4,x-4,x-4,x-4,x-5,x-5,x-5,x-5,x-5,x-5,x-5,x-5]
  yh = [7,8,9,10,11,12,7,8,9,10,11,12,7,8,9,10,11,12,13,14,7,8,9,10,11,12,13,14,9,10,11,12,13,14,15,16,9,10,11,12,13,14,15,16]
  b = 0 
  while b < 44:
    set_pixel(xh[b],yh[b],(255,0,0))
    b+=1
  
def fillheart2(x):
  xh = [x,x,x,x,x,x,x,x,x-1,x-1,x-1,x-1,x-1,x-1,x-1,x-1,x-2,x-2,x-2,x-2,x-2,x-2,x-2,x-2,x-3,x-3,x-3,x-3,x-3,x-3,x-3,x-3,x-4,x-4,x-4,x-4,x-4,x-4,x-5,x-5,x-5,x-5,x-5,x-5]
  yh = [9,10,11,12,13,14,15,16,9,10,11,12,13,14,15,16,7,8,9,10,11,12,13,14,7,8,9,10,11,12,13,14,7,8,9,10,11,12,7,8,9,10,11,12]
  b = 0
  while b < 44:
    set_pixel(xh[b],yh[b],(255,0,0))
    b+=1

def allheart(vie,heartP):
  affheart(heartP)
  a = 0
  x1 = 372
  x2 = 366
  while a < vie:
    fillheart1(x1)
    a+=1
    if a == vie:
      return 0
    x1 = x1-18
    fillheart2(x2)
    a+=1
    if vie == a:
      return 0
    x2 = x2-18


hideturtle()

r = (255,0,0)
def apple(x,y):
  set_pixel(x-1,y+1,r)
  set_pixel(x,y+1,r)
  set_pixel(x+1,y+1,r)
  set_pixel(x+1,y,r)
  set_pixel(x,y,r)
  set_pixel(x-1,y,r)
  set_pixel(x-1,y-1,r)
  set_pixel(x,y-1,r)
  set_pixel(x+1,y-1,r)
  

def direction():
  d = getkey()
  if d == 23:
    setheading(180)
  elif d == 25:
    setheading(0)
  elif d == 14:
    setheading(90)
  elif d == 34:
    setheading(-90)
    
def ifapplebite(x,y):
  if get_pixel(x-1,y) != (248,0,0):
    return 1
  elif get_pixel(x,y) != (248,0,0):
    return 1
  elif get_pixel(x+1,y) != (248,0,0):
    return 1
  elif get_pixel(x-1,y-1) != (248,0,0):
    return 1
  elif get_pixel(x,y-1) != (248,0,0):
    return 1
  elif get_pixel(x+1,y-1) != (248,0,0):
    return 1
  elif get_pixel(x-1,y+1) != (248,0,0):
    return 1
  elif get_pixel(x,y+1) != (248,0,0):
    return 1
  elif get_pixel(x+1,y+1) != (248,0,0):
    return 1
  else:
    return 0


#def accueil():
def accueil():
  draw_string(150,71,"Snake",(0,255,0),"large")  
  draw_string(110,140,"Press [EXE] to start")
  show_screen()
  
def accueil2():
  accueil()
  a = 0
  while a == 0:
    if getkey()==95:
      a+=1
      clear_screen()
 
def cadre():
  w = 0
  j = 30
  while w < 390:
    set_pixel(w,j)
    w+=1
    
  
   
def main():
  v=vie
  t=0
  pensize(5)  
  x = randint(10,370)
  y = randint(35,180)
  b=0
  pencolor("green")
  accueil2()
  penup()
  goto(0,-20)
  pendown()
  while v != 0:
    cadre()
    allheart(v,heartP)
    p = str(t)
    draw_string(10,7,"Score :")
    draw_string(80,7,p)
    apple(x,y)
    forward(5)
    direction()
    b+=1
    s = 0
    k = ifapplebite(x,y)
    if k == 1:
      t+=1
      x = randint(10,370)
      y = randint(35,180)
      apple(x,y)
    if position()[0]<-189:
      v-=2
      penup()
      goto(0,-20)
      pendown()
    elif position()[0]>189:
      v-=2
      penup()
      goto(0,-20)
      pendown()
    elif position()[1]>64:
      v-=2
      penup()
      goto(0,-20)
      pendown()
    elif position()[1]<-94:
      v-=2
      penup()
      goto(0,-20)
      pendown()
    if b>1:
      clear_screen()
      b=0  
      
  clear_screen()
  draw_string(120,91,"Game over",(255,0,0),"large")
  draw_string(150,130,"Score :")
  draw_string(215,130,p)
        

show_screen()
main()

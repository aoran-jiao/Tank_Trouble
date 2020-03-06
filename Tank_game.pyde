add_library('box2d_processing')
add_library("minim")

'''
from game2dai.entities. import * # AI for 2d games library
import game2dai.entityshapes.ps.
import game2dai.maths.
import game2dai.
import game2dai.entityshapes.
import game2dai.fsm.
import game2dai.steering.
import game2dai.utils.
import game2dai.graph.
'''

from random import randint
# import pickle
bullet2 = [] # array of bullets for player 2
bullet1 = [] # array of bullets for player 1
import player1
from player1 import *
p1c = 1
p1 = Player1(p1c)

import player2
from player2 import *
keyss = [False, False, False, False]
p2c = 1
p2 = Player2(keyss, p2c)

import bullet
from bullet import *

b1x = 1 # p1.location.x
b1y = 1 # p1.location.y
b1 = Bullet(b1x, b1y, 2, 3, 255, 0, 0)
bb1 = False # controlling player 1
b2x = 1
b2y = 1
b2 = Bullet(b2x, b2y, 2, 3, 0, 0, 255)
bb2 = False # controlling player 2

import maze
from maze import *
m = Maze(1000/2-370, 800/2-380, 750, 6) # maze data: x location, y location, size, level(complexity)
m1 = Maze(1000/2-370, 800/2-380, 750, 7) # more complex
m2 = Maze(1000/2-370, 800/2-380, 750, 8) # top complex

# m = m2
finished = False
timer = millis()

import modes 
from modes import *
mod = Mode(p1, p2)

from score import *

score1 = Score(p1.choice)
score2 = Score(p2.choice)

# Game interphase
mode = 0 # 0: title page; 1: game mode; 2: instructions; 3: choose your tank player 1; 4: choose your tank player 2; gameover1/gameover2

sizemode = 1 # normal mode; 2 = P3D

TEXT_SPEED = 0.5
y = 840
thank = ""

def setup():
  global tank1, tank2, tank3, tank4, bs, bu, tm, win, transform
  global sizemode
  global logs, y, thank
  
  logs = loadStrings("thank.txt") # read file
  for l in logs: 
      thank += l + "\n"
  
  size(1000, 800)
     
  # fullScreen()
  
  tank1 = loadImage("tank1.png")
  tank2 = loadImage("tank2.png")
  tank3 = loadImage("tank3.png")
  tank4 = loadImage("tank4.png")
  
  minim = Minim(this)
  bs = minim.loadFile("bullet1.wav")
  bu = minim.loadFile("laser.wav")
  tm = minim.loadFile("tanknew.mp3")
  win = minim.loadFile("win.wav")
  transform = minim.loadFile("transform.mp3")
  
  frameRate(100)
      
def draw(): 
  global b1, bb1, b2, bb2, p1, p2, b1x, b1y, mode
  global bullet1, bullet2
  global score1, score2, scorechoice1, scorechoice2
  global bs, bu, win, transform
  global p1c, p2c
  global y, logs # thank you mode

  
  if mode == 1: # game mode
     background(255)
    # maze generation + transforming sound
     if not m.complete:
        transform.rewind()
        transform.play() 
        m.routeStep()
        
     else:
        if not finished:
            background(255)
            m.display()
        
     imageMode(CENTER)
     image(tank1, 50, 700, 80, 80)
     image(tank2, 950, 700, 80, 80)
                
     # test = m.travelThrough(getPoint(mouseX, mouseY)[0], getPoint(mouseX, mouseY)[1]) # test maze wall function
     # print(test)
     # walls = m.travelThrough(getPoint(p2.x, p2.y)[0], getPoint(p2.x, p2.y)[1])
     
  
     p1.update() # player 1 tank
     p1.display()
     p1.corner()
     
     p2.update() # player 2 tank
     p2.display()
     p2.corner()
     

     score1.choice = p1.choice
     score2.choice = p2.choice
     
     score1.display(p1.location.x, p1.location.y)
     score2.display(p2.x, p2.y)
     
     score1.store(2) # display p1 and p2 overall score
     score2.store(1)
     
     # collisions with tanks
     if p1.choice == p2.choice: # equal mass tanks
        p2.collide(p1.location, 5)
        
     elif p1.choice > p2.choice: # p1 is heavier than p2
         p2.collide(p1.location, 3)
         
     elif p2.choice > p1.choice: # p2 is heavier than p1
         p2.collide(p1.location, 7)

     if bb2 == True:
        for i in bullet2: # keyboard control player 2 bullet
         
          i.display()
          i.move()
          i.corner()
          i.vanish()
          
          
        # if i.vanish() == True:
            # bullet2.del(bullet2.index(i))
            
          if i.overlap(p1.location) == True: # p2 hit on p1
             score1.update(2) # update p2's score, increment by 1
             bs.rewind()
             bs.play()
          if i.overlap(p2) == True: # p2 hit on p2
             score2.update(1) # update p1's score, increment by 1
             bs.rewind()
             bs.play()
             
          # b2walls = m.travelThrough(getPoint(i.x, i.y)[0], getPoint(i.x, i.y)[1])
          # print(b2walls)       
    
     if bb1 == True: # mouse control player 1 bullet
         for i in bullet1: # the array of bullets, continuous shooting
             
            i.display()
            i.move()
            i.corner()
            i.vanish()
            
            # if i.vanish() == True:
                # bullet1.del(bullet1.index(i))
            
            if i.overlap(p1.location) == True: # p1 hit on p1
                score1.update(2) # decrease p1 blood bar; increase p2 score
                bs.rewind()
                bs.play()
            if i.overlap(p2) == True: # p1 hit on p2
                score2.update(1) # decrease p2 blood bar; increase p1 score
                bs.rewind()
                bs.play()
      
     if score1.w == 0: # p1 has no blood
                mode = "gameover1"
                win.rewind()
                win.play()
          
     elif score2.w == 0: # player 2 has no blood
                mode = "gameover2"
                win.rewind()
                win.play()
    
                
         
  elif mode == 0: # title mode page
      mod.mode0()
      # p2.drive(800, 800, randint(2, 4), randint(2, 4))

  elif mode == 2: # instruction mode
      mod.mode2()
      

  elif mode == 3: # choose your tank for player 1 (red)
        mod.mode3()
            
        
  elif mode == 4: # choose your tank for player 2 (blue)
      mod.mode4() 
        
  elif mode == "gameover1":
    mod.gameover(2) # player 2 wins
    reset()
        
  elif mode == "gameover2":
        mod.gameover(1) # player 1 wins
        reset()
        
  elif mode == "pvc":
      mod.pvc()
      
  elif mode == 10:
      background(0)
      translate(width/2,height/2)
  
      fill(250,250,0) # yellow color of text
      textAlign(CENTER,CENTER)
      textSize(40)
      text(thank, 0, y)
      y -= TEXT_SPEED
     
  elif mode == "level1":
      mod.level1()
      

     
def reset(): # reset the game
    global p1, p2, bullet1, bullet2, score1, score2
    p1.location = PVector(randint(170, 200), randint(60, 110))
    p1.velocity = PVector(0, 0)
    p2.x, p2.y = randint(800, 820), randint(680, 720)
    p2.r = 0
    bullet1 = []
    bullet2 = []
    score1.reset()
    score2.reset()
    
def keyReleased(): # player 2 control for continuous moving
    global keyss, bb2, bullet2, mode
    if key =="w":
        keyss[0] = False
    
    if key == "s":
        keyss[1] = False
        
    if key == "a":
        keyss[2] = False

    if key == "d":
        keyss[3] = False
        
def getPoint(x, y): # function to help detect wall conditions of a cell
    l =[] # 2d array
    lx = []
    ly = []
    disl = []
    
    for i in range(6):
        lx.append(130 + m.step/2 + m.step * i)
     
    for i in range(6):
        ly.append(20 + m.step/2 + m.step * i)
        
    for i in lx:
        for j in ly:
            l.append([x, y, i, j]) # creating 2d array
            dis = dist(x, y, i, j)
            disl.append(dis)
            e = min(disl)
            ind = disl.index(e)
            rx = l[ind][2]
            ry = l[ind][3]
    
    
    return rx, ry  # the closest center of cell to the current position
                

def keyPressed():
    global keyss, b2, bb2, b2x, b2y, p2, p1, bullet2, m, getPoint, mode
    global y, logs
    
    walls = m.travelThrough(getPoint(p2.x, p2.y)[0], getPoint(p2.x, p2.y)[1])
    print(walls)
    
    for i in range(4): # bounce off walls
        if walls[0] == True: # wall upwards
           du = abs((getPoint(p2.x, p2.y)[1] - (750 // 12)) - p2.y)
           print(du)
           if du <= 35:
              p2.bounce("u")
           
        if walls[1] == True: # wall downwards
            dd = abs((getPoint(p2.x, p2.y)[1] + (750 // 12)) -  p2.y)
            print(dd)
            if dd <= 35:
                p2.bounce("d")
            
        if walls[2] == True: # wall left
            dl = abs((getPoint(p2.x, p2.y)[0] - (750 // 12)) - p2.x)
            print(dl)
            if dl <= 35:
                p2.bounce("l")
            
        if walls[2] == True: # wall right
            dr = abs((getPoint(p2.x, p2.y)[0] + (750 // 12)) - p2.x)
            print(dr)
            if dr <= 35:
                p2.bounce("r")
            
            
            
    # counter = 0 # count the number of bullets fired
    if mode == 1:
        
        if key =="w": # move forward
          # if not walls[0]: # forward has a wall
            keyss[0] = True
            tm.rewind()
            tm.play()
    
        elif key == "s": # move backward
        # if not walls[1]: # backward has a wall
            keyss[1] = True
            tm.rewind()
            tm.play()
        
        elif key == "a": # turn left
        # if not walls[2]: # left has a wall
            keyss[2] = True
            tm.rewind()
            tm.play()
            
        elif key == "d": # turn right
        # if not walls[3]: # right has a wall
            keyss[3] = True
            tm.rewind()
            tm.play()
        
        elif key == "q": # player 2 keyboard control fire bullet
        # counter += 1
            bb2 = True
            bu.rewind()
            bu.play()
            
            #b2.x = p2.x + cos(radians(p2.r - 90)) * 50 # let the bullet shoot directly from the cannon
            #b2.y = p2.y + sin(radians(p2.r - 90)) * 50
            #b2.xspeed = cos(radians(p2.r - 90)) * 8
            #b2.yspeed = sin(radians(p2.r - 90)) * 8
            
            b2 = Bullet(p2.x + cos(radians(p2.r - 90)) * 50, p2.y + sin(radians(p2.r - 90)) * 50,  cos(radians(p2.r - 90)) * 8, sin(radians(p2.r - 90)) * 8, 0, 0, 255)
        
            bullet2.append(b2) # p2 bullet objects array
            
            # if len(bullet2) != 0 and (len(bullet2) % 5) == 0: # every 5 bullets, stop for 3 seconds to reload
                 # bb2.reload()
        
    if key == "n": # secret message
        mode = 10
      
    if key == "r":
        m = m1
        
    if key == "t":
        m = m2       
        
    if key == "l":
        m = m
         
def mousePressed():
    print(mouseX, mouseY)
    global bb1, mode, tchoice1, tchoice2, m, bullet1, bs
    global p1c, p2c
    
    if mode == 1: # game mode
        bb1 = True    # player 1 fire bullet
        bu.rewind()
        bu.play()
        # b1.x = p1.location.x + cos(atan2(p1.mouse.y, p1.mouse.x)) * 50 # bullets shooting directly from cannon
        # b1.y = p1.location.y + sin(atan2(p1.mouse.y, p1.mouse.x)) * 50
        # b1.xspeed = p1.mouse.setMag(10).x
        # b1.yspeed = p1.mouse.setMag(10).y
        
        b1 = Bullet(p1.location.x + cos(atan2(p1.mouse.y, p1.mouse.x)) * 50, p1.location.y + sin(atan2(p1.mouse.y, p1.mouse.x)) * 50, p1.mouse.setMag(10).x, p1.mouse.setMag(10).y, 255, 0, 0)
        bullet1.append(b1)
    
    if mode == 0: # at main page; rect(width/2, height/2, 200, 100) # button 
        if mouseX >= width/2 - 100 and mouseX <= width/2 + 100 and mouseY >= height/2 - 50 and mouseY <= height/2 + 50: 
            mode = 1
        
        elif mouseX >= width/2 - 100 and mouseX <= width/2 + 100 and mouseY >= height/2 + 100 and mouseY <= height/2 + 200: # rect(width/2, height/2 + 150, 200, 100, 5)
            mode = 2
        
        elif mouseX >= width/2 - 290 and mouseX <= width/2 - 110 and mouseY >= height/2 - 250 and mouseY <= height/2 - 150: # ellipse(width/2 - 200, height/2 - 200, 180, 100): tank choice for player 1
            mode = 3
            
        elif mouseX >= width/2 + 110 and  mouseX <= width/2 + 290 and mouseY >= height/2 - 250 and mouseY <= height/2 - 150: # tank choice for player 2
            mode = 4
            
        elif mouseX >= 100 and mouseX <= 300 and mouseY >= 550 and mouseY <= 650:  # rect(200, 600, 200, 100, 5)
            mode = "pvc"
            
    if mode == 2 or mode == 3 or mode == 4 or mode == "gameover1" or mode == "gameover2" or mode == "pvc" or mode == "level1": # exit for all pages at instruction page: button: rect(width - 100, height - 100, 150, 100, 30)
        if mouseX >= width - 175 and mouseX <= width - 25 and mouseY >= height - 150 and mouseY <= height - 50:
            mode = 0 # return to main page
            
    if mode == 3: # player 1 red choose the tank 
        
        if mouseX >= 600 and mouseX <= 850 and mouseY >= 190 and mouseY <= 470: # 600, 190, 250, 280 
            p1.choice = 2 # change to another tank choice
            
        
        elif mouseX >= 150 and mouseX <= 400 and mouseY >= 200 and mouseY <= 450: # 150, 200, 250, 250
            p1.choice = 1
            
        
    
    if mode == 4: #  player 2 blue choose the tank
            
        if mouseX >= 600 and mouseX <= 850 and mouseY >= 190 and mouseY <= 470: # 600, 190, 250, 280 
            p2.choice = 2 # change to another tank choice
            
            
        elif mouseX >= 150 and mouseX <= 400 and mouseY >= 200 and mouseY <= 450:
            p2.choice = 1
            
    if mode == "pvc":
        if mouseX >= 40 and mouseX <= 240 and mouseY >= 150 and mouseY <= 250:     # rect(140, 200, 200, 100, 5)
            mode = "level1"
      
    
        
            

            
            
        
            
            
        
    
    
    
    
    
    


        

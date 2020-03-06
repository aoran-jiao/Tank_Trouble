from random import randint
class Player2(object): # keyboard control

    def __init__(self, keyss, choice):
        self.x, self.y = randint(800, 820), randint(680, 720)
        self.r = 0
        
        self.keyss = keyss # control player 2
        self.choice = choice
        #self.pic = pic
        
    def update(self):
        if self.choice == 1: # light weight tank
          if self.keyss[0] == True:
            self.x += cos(radians(self.r - 90)) * 6
            self.y += sin(radians(self.r - 90)) * 6

          if self.keyss[1] == True:
            self.x -= cos(radians(self.r - 90)) * 6
            self.y -= sin(radians(self.r - 90)) * 6
        
          if self.keyss[2] == True:
            self.r -= 3
        
          if self.keyss[3] == True:
            self.r += 3
            
        elif self.choice == 2: # heavy weight tank
            if self.keyss[0] == True:
                self.x += cos(radians(self.r - 90)) * 5
                self.y += sin(radians(self.r - 90)) * 5

            if self.keyss[1] == True:
                self.x -= cos(radians(self.r - 90)) * 5
                self.y -= sin(radians(self.r - 90)) * 5
        
            if self.keyss[2] == True:
                self.r -= 5
        
            if self.keyss[3] == True:
                self.r += 5
            
    
    def display(self):
          pushMatrix()
          translate(self.x, self.y)
          rotate(radians(self.r))
          imageMode(CENTER)
          
          if self.choice == 1:
              image(loadImage("tank2.png"), 0, 0, 70, 70)
          elif self.choice == 2:
              image(loadImage("tank4.png"), 0, 0, 70, 70)
              
          popMatrix()
          
    def corner(self): # to be updated, drive inside the maze
    
        
        if self.x - 35 < 130:
            self.x += 8
            
        if self.x + 35 > 880:
            self.x -= 8
            
        if self.y + 35 > 770:
            self.y -= 8
            
        if self.y - 35 < 20:
            self.y += 8
        
    def collide(self, other, mass): # mass reflects the mass of self object
        if dist(self.x, self.y, other.x, other.y) <= 60: # if player2 collide with something else, equal mass
            loc = PVector(self.x, self.y)
            locother = PVector(other.x, other.y)
            loc.sub(locother) # direction of self object motion
            self.x += loc.setMag(5).x # self object bounce off
            self.y += loc.setMag(5).y
            
            
            other.x -= loc.setMag(mass).x # other object bounce off (self is heavier: mass = 7, self is lighter: mass = 3, self and other equal mass: mass = 5)
            other.y -= loc.setMag(mass).y
              
    def drive(self, x, y, xspeed, yspeed):
        image(loadImage("tank2.png"), x, y, 70, 70)
        while True:
            x -= xspeed
            y -= yspeed
        
        if x - 35 < 0 or x + 35 > 1000:
            xspeed *= -1
            
        if y + 35 > 800 or y - 35 < 0:
            yspeed *= -1
      
    def bounce(self, di):
        if di == "u":
            self.y += 8
        if di == "d":
            self.y -= 8
            
        if di == "l":
            self.x += 8
            
        if di == "r":
            self.x -= 8
            
           
            
            
            
            
            
            
            
            
          

            
            
            
            

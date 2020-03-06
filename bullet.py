class Bullet(object):
    sc = 0
    shoott = 0
   
    def __init__(self, x, y, xspeed, yspeed, r, g, b):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.r = r # color
        self.g = g
        self.b = b
        
                
    def display(self):
        
        strokeWeight(10.0)
        stroke(100, 100)
        fill(self.r, self.g, self.b)
        ellipse(self.x, self.y, 8, 8) # size of the bullet
 
        
    def move(self):
        
        self.x += self.xspeed
        self.y += self.yspeed
   
    def corner(self):
   
            if self.x <= 135 or self.x >= 875:
                self.xspeed *= -1
            
            if self.y <= 25 or self.y >= 765:
                self.yspeed *= -1
            
    def vanish(self): # timing function for bullets 

            if self.shoott == 0 :
                self.shoott = millis()
            self.sc = millis()
        
            if (self.sc - self.shoott) // 1000 > 4: # the time after the bullet is shot; each last for 4 seconds 
                self.xspeed = 0
                self.yspeed = 0
                self.x, self.y = -100, -100

                self.shoott = 0
                # return True
                
             
    def overlap(self, other):
        if dist(self.x, self.y, other.x, other.y) <= 35:
            self.xspeed, self.yspeed = 0, 0
            self.x, self.y = -100, -100
            return True
        
    def reload(self):
        pass
        
        
        
    # def bounce(self, other): # collide and bounce off walls
            
        
        
        
        
        
        
        
    

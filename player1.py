from random import randint

class Player1(object): # mouse control
    
    def __init__(self, choice):
        
        self.location = PVector(randint(170, 200), randint(60, 110))
        self.velocity = PVector(0, 0)

        self.choice = choice
        
        self.bx = self.location.x
        self.by = self.location.y
        self.bspeedx = 2
        self.bspeedy = 3
        
    def update(self):
        
        self.mouse = PVector(mouseX, mouseY)
        a = self.mouse.sub(self.location) # direction of turning
        # self.location.add(a.setMag(6)) # acceleration, how to make constant velocity
        self.location.add(a.mult(0.03))
        
    
    def display(self):
        
        pushMatrix()
        translate(self.location.x, self.location.y)
        
        rotate(radians(90) + atan2(self.mouse.y, self.mouse.x))
        
        imageMode(CENTER)
        if self.choice == 1: # light tank
            image(loadImage("tank1.png"), 0, 0, 70, 70)
        
        elif self.choice == 2: # heavy tank
            image(loadImage("tank3.png"), 0, 0, 60, 70)
           
        popMatrix()

    def corner(self): # drive inside the maze
        if self.location.x - 35 < 130:
            self.location.x += 5
            
        if self.location.x + 35 > 880:
            self.location.x -= 5
            
        if self.location.y + 35 > 770:
            self.location.y -= 5
            
        if self.location.y - 35 < 20:
            self.location.y += 5
        
    def bounce(self, di):
        if di == "u":
            self.y += 8
        if di == "d":
            self.y -= 8
            
        if di == "a":
            self.x += 8
            
        if di == "d":
            self.x -= 8
            
        
        
        
        
        

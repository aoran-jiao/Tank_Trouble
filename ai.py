class ai(object):
    def __init__(self):
        self.x = width/2
        self.y = 100
        
    def display(self):
        
        imageMode(CENTER)
        image(loadImage("tank4.png"), self.x, self.y, 200, 200)
        
    def calculate(self, x, y): # detect the position of the player by the computer
        
        

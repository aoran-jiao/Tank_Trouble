from player1 import *
from player2 import *
class Score():
    def __init__(self, choice):
        
        self.choice = choice # which level tank you choose
        
        if self.choice == 1:
            self.w = 50 # amount of blood is 50
        elif self.choice == 2:
            self.w = 80 # amount of blood is 80
        
        # self.w = 0
        self.s1 = 0
        self.s2 = 0
        
    def display(self, x, y):
        
        fill(255, 0, 0)
        noStroke()
    
        rect(x - 40, y + 40, self.w, 10, 3)
        
    def update(self, c):
        
        self.w -= 10 
        if c == 1:
            self.s1 += 1
        
        if c == 2:
            self.s2 += 1
            
        
    def reset(self):
        
        self.w = 50
        
    def store(self, ch): # show on page the overall score of the two players
        
        textMode(CENTER)
        textSize(16)
        if ch == 1:
            fill(255, 0, 0)
            text("SCORE: " + str(self.s1), 20, 650) # player 1 score
            
        elif ch == 2:    
            fill(0, 0, 255)
            text("SCORE: " + str(self.s2), 920, 650) # player 2 score
    
    
    

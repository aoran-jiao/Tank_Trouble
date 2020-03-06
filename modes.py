from player2 import *
class Mode(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
        
    def exitb(self):
        rectMode(CENTER)
        noStroke()
        fill(255, 255, 0)
        rect(width - 100, height - 100, 150, 100, 30) # button for exit to main page
        fill(0)
        text("Exit", width - 150, height - 80)
        
    def mode0(self): # title page
       background(255)
       
       textMode(CENTER) 
       textSize(50)
       strokeWeight(6)
       if (frameCount / 60) % 2 == 0: # flashing effect
          fill(255, 0, 0)
       else:
           fill(0, 0, 255)
    
       text("Tank Trouble", width/2 - 150, height/2 - 300) # title
    
       rectMode(CENTER)
       noFill()
       stroke(0)
       strokeWeight(1)
       rect(width/2, height/2, 200, 100, 5) # button play
       fill(0, 0, 255)
       textSize(60)
       # textMode(CENTER)
       text("PLAY", width/2 - 70, height/2 + 30)
       
       noFill()
       stroke(0)
       strokeWeight(1)
       rect(width/2, height/2 + 150, 200, 100, 5) # button instructions
       fill(0, 0, 255)
       textSize(30)
       text("Instructions", width/2 -80, height/2 + 160)
       
       noFill()
       stroke(0)
       strokeWeight(1)
       rect(200, 600, 200, 100, 5) # button instructions

       textSize(18)
       fill(178, 17, 242)
       text("Computer V.S. Player", 105, 600) # button alternative choice
       
       ellipseMode(CENTER) # button for player 1 red
       fill(255, 0, 0, 120)
       stroke(100)
       strokeWeight(1)
       ellipse(width/2 - 200, height/2 - 200, 180, 100)
       fill(255)
       textMode(CENTER)
       textSize(30)
       text("Player1", width/2 - 250, height/2 - 190)
       
       pushMatrix() # button for player 2 blue
       translate(400, 0)
       fill(0, 0, 255, 120)
       stroke(100)
       strokeWeight(1)
       ellipse(width/2 - 200, height/2 - 200, 180, 100)
       fill(255)
       textMode(CENTER)
       textSize(30)
       text("Player2", width/2 - 250, height/2 - 190)
       popMatrix()
       
       
       
       textMode(CENTER)
       fill(0, 255, 0)
       stroke(1)
       text("Press 'esc' to finish the game", width/2, height - 80)

    def mode2(self): # instruction mode
      background(255)
      textSize(50)
      textMode(CENTER)
      fill(0)
      text("Instruction", width/2 - 150, 60)
      
      textMode(CENTER)
      text("Player 1", 100, 300)
      text("Player 2", width - 300, 300)

      
      ellipseMode(CENTER)
      ellipse(320, 370, 10, 10)
      textSize(20)
      text("To control direction", 340, 390)
      
      rectMode(CENTER)
      fill(255)
      stroke(5)
      rect(200, 390, 100, 100, 8)
      fill(0)
      textMode(CENTER)
      textSize(40)
      text("W", 180, 415)
      
      pushMatrix()
      translate(0, 120)
      fill(255)
      stroke(5)
      rect(200, 390, 100, 100, 8)
      fill(0)
      textMode(CENTER)
      textSize(40)
      text("S", 190, 415)
      popMatrix()
      
      pushMatrix()
      translate(120, 120)
      fill(255)
      stroke(5)
      rect(200, 390, 100, 100, 8)
      fill(0)
      textMode(CENTER)
      textSize(40)
      text("D", 180, 415)
      popMatrix()
      
      pushMatrix()
      translate(-120, 120)
      fill(255)
      stroke(5)
      rect(200, 390, 100, 100, 8)
      fill(0)
      textMode(CENTER)
      textSize(40)
      text("A", 180, 415)
      popMatrix()
      
      pushMatrix()
      translate(-100, 300)
      fill(255)
      stroke(3)
      rect(200, 390, 100, 100, 8)
      fill(0)
      textMode(CENTER)
      textSize(40)
      text("Q", 180, 415)
      
      ellipseMode(CENTER)
      ellipse(320, 380, 10, 10)
      fill(0)
      stroke(3)
      textSize(40)
      text("To shoot", 350, 400)
      
      popMatrix()
      
      imageMode(CENTER)
      image(loadImage("mouse.png"), 800, 500, 200, 250)
      
      ellipseMode(CENTER)
      ellipse(650, 360, 10, 10)
      textMode(CENTER)
      textSize(20)
      text("Mouse to control direction", 700, 370)
      
      ellipseMode(CENTER)
      ellipse(482, 682, 10, 10)
      textSize(40)
      text("Click to shoot", 500, 700)

      
      self.exitb()
      

    def mode3(self):
        background(255)
        textSize(50)
        textMode(CENTER)
        fill(0)
        text("Choose your tank, Player 1", width/2 - 300, 90)
        # exit button
        self.exitb()
        
        imageMode(CORNER)
  
        image(loadImage("tank1.png"), 150, 200, 250, 250)
        image(loadImage("tank3.png"), 625, 200, 200, 250)
        
        textMode(CENTER)
        textSize(40)
        fill(255, 0, 0)
        text("Speed: 10", 200, 510)
        text("Health: 5", 200, 600)
        text("Attack: 5", 200, 700)
        
        text("Speed: 8", 650, 510)
        text("Health: 7", 650, 600)
        text("Attack: 3", 650, 700)
        
        if self.p1.choice == 1:
            rectMode(CORNER)
            fill(100, 50)
            rect(150, 190, 250, 270, 10)
            
        elif self.p1.choice == 2:
            rectMode(CORNER)
            fill(100, 50)
            rect(600, 190, 250, 280, 10)
      
    def mode4(self):
        background(255)
        textSize(50)
        textMode(CENTER)
        fill(0)
        text("Choose your tank, Player 2", width/2 - 300, 90)
        # exit button
        self.exitb()
        
        imageMode(CORNER)

        image(loadImage("tank2.png"), 150, 200, 250, 250)
        image(loadImage("tank4.png"), 600, 190, 250, 280)
        
        textMode(CENTER)
        textSize(40)
        fill(0, 0, 255)
        text("Speed: 10", 200, 510)
        text("Health: 5", 200, 600)
        text("Attack: 5", 200, 700)
        
        text("Speed: 5", 650, 510)
        text("Health: 7", 650, 600)
        text("Attack: 8", 650, 700)
        
        if self.p2.choice == 1:
            rectMode(CORNER)
            fill(100, 50)
            rect(150, 190, 250, 270, 10)
            
        elif self.p2.choice == 2:
            rectMode(CORNER)
            fill(100, 50)
            rect(600, 190, 250, 280, 10) 

    def gameover(self, n):
        
        imageMode(CORNER)
        image(loadImage("victory.png"), 0, 0, width, height)
        fill(255, 0, 0)
        textMode(CENTER)
        fill(255, 0, 0)
        textSize(35)
        text("Game Over", width/2, height/2) 
        
        if n == 1:
            fill(255, 0, 0)
            text("Player " + str(n) + " wins! ", width/2, height/2 + 200)
            
        elif n == 2:
            fill(0, 0, 255)
            text("Player " + str(n) + " wins! ", width/2, height/2 + 200)
            
            
        self.exitb()
        
    def pvc(self):
        # tint(255, 127)
        imageMode(CORNER)
        image(loadImage("pvc.png"), 0, 0, width, height)
        fill(0)
        rect(140, 200, 200, 100, 50)
        fill(255)
        text("Level 1", 100, 210)
        self.exitb()
        
    
    def level1(self):
        background(255)
        
        
        self.exitb()
        

        
      

    
        
        
       








        
        

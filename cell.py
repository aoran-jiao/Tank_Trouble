class Cell(object):
  def __init__(self, x, y, w):
       self.x = x 
       self.y = y
       self.w = w
       self.walls = [True, True, True, True] # cell walls to be broken to form the maze
       self.visited = 0
       self.marked = False
        
 
  def display(self, weight):
    noStroke()
    fill(255 - self.visited, 0)
    rect(self.x + weight/2, self.y + weight/2, self.w - weight, self.w - weight) # draw each rectangle as a cell
    stroke(0)
    strokeWeight(weight)
 
    if self.walls[0]:
      line(self.x, self.y, self.x + self.w, self.y)
      
    if self.walls[1]:
      line(self.x, self.y + self.w, self.x + self.w, self.y + self.w)
      
    if self.walls[2]:
      line(self.x,self.y,self.x,self.y + self.w)
      
    if self.walls[3]:
      line(self.x+self.w,self.y,self.x+self.w,self.y+self.w)
  
 
  def reset(self):
      for i in range(4):
          self.walls[i] = True
          
      self.visited = 0

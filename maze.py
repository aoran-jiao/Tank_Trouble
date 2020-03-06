from cell import *
from random import randint

class Maze(object):
    
  def __init__(self, x, y, w, ca):
        self.x = x # length of the maze
        self.y = y # width of the maze
        self.w = w # size of the maze
        self.cellsAcross = ca # complexity of the maze
        
        self.cells = []
        self.totalCells = self.cellsAcross ** 2
        self.visitedCells = 1
        self.currentCell = self.totalCells - 1
        self.cellStack = []
        self.step = self.w/self.cellsAcross
        
        self.complete = False
        
        for i in range(self.cellsAcross):
            for j in range(self.cellsAcross):
                c = Cell(self.x + j * self.step, y + i * self.step, self.step)
                self.cells.append(c)
 
  
 
        self.destinationX = self.x + self.w - self.step
        self.destinationY = self.y + self.w - self.step
        
        self.lastCell = self.cells[len(self.cells)-1]  # Cell lastCell=(Cell) cells.get(cells.size()-1)
        self.lastCell.marked = True
 
  def reset(self, ca):
 
    self.cellsAcross = ca
    
    for i in range(len(self.cells) - 1, -1, -1):
        self.cells.remove(i)    
        
    for i in range(self.cellAcross):
        for j in range(self.cellAcross):
            c = Cell(self.x + j * self.step, y + i * self.step, self.step)
            self.cells.append(c) 
            
 
 
    self.lastCell = self.cells.index(self.cells[-1])  # Cell lastCell=(Cell) cells.get(cells.size()-1)
    self.lastCell.marked = True
 
    while len(self.cellStack)>1: 
      self.cellStack = shorten(cellStack)
    
    self.totalCells = self.cellsAcross ** 2
    self.visitedCells = 1
    self.currentCell = self.totalCells - 1
    self.cellStack[0] = self.currentCell
    self.destinationX = self.x + self.w - self.step
    self.destinationY = self.y + self.w - self.step

        
    self.complete = False
    self.finished = False
        
    randomSeed(millis())
 
 
  def display(self):
      
    for i in range(len(self.cells)):
        self.c = self.cells[i]
        self.c.display(self.step/8)
        
 
  def travelThrough(self, x, y):
 
    ind = self.cellsAcross * ((y - self.y)/self.step) + ((x - self.x)/self.step)
    inCell = self.cells[ind] # (Cell) cells.get(index) getting an element at a specific index
    inCell.visited = min(255, inCell.visited+65) # that perticular cell is going to be painted darker till 0
    return inCell.walls # return the boolean variable
  
 
  def routeStep(self):
 
    # find the current cell's neighbors
    numberOfPossibles = 0
 
    neighbors = [self.currentCell-self.cellsAcross,self.currentCell+self.cellsAcross,self.currentCell-1,self.currentCell+1]

 
    # check for edges
    if self.currentCell-self.cellsAcross < 0:
        neighbors[0]=-1
    if self.currentCell+self.cellsAcross>=self.cellsAcross*self.cellsAcross:
        neighbors[1]=-1
    if self.currentCell % self.cellsAcross == 0 :
        neighbors[2]=-1
    if self.currentCell % self.cellsAcross == self.cellsAcross-1:
        neighbors[3]=-1
 
    # check for previously visited cells
    for i in range(4):
        if neighbors[i]!=-1:
            c = self.cells[neighbors[i]]   # Cell c = (Cell) cells.get(neighbors[i])
            if c.marked:
                neighbors[i]=-1
            else:
                numberOfPossibles += 1
                
                
    if numberOfPossibles>0: 
      
      chosenCell = randint(0, numberOfPossibles)
      
      for i in range(4):
        if neighbors[i]!=-1:
          if chosenCell==0:
            # this is the next cell
            thisCell = self.cells[self.currentCell]
            nextCell = self.cells[neighbors[i]]
            thisCell.marked=True
            nextCell.marked=True
            # let's knock down the 2 adjoining walls
            if i==0:
              thisCell.walls[0]=False
              nextCell.walls[1]=False
            
            if i==1:
              thisCell.walls[1]=False
              nextCell.walls[0]=False
            
            if i==2: 
              thisCell.walls[2]=False
              nextCell.walls[3]=False
            
            if i==3: 
              thisCell.walls[3]=False
              nextCell.walls[2]=False
            
            self.visitedCells += 1
            
            if self.visitedCells == self.totalCells:
              self.complete=True
              # print(millis()-timer)
            
            self.currentCell = neighbors[i]
            self.cellStack.append(self.currentCell)
            stroke(0,0,255,5+250*thisCell.x/width)
            strokeWeight(self.step/2)
            w = width/(self.cellsAcross*2)
            line(thisCell.x+self.step/2,thisCell.y+self.step/2,nextCell.x+self.step/2,nextCell.y+self.step/2)
            break
          
          else:
            chosenCell -= 1
    
    else:
      self.currentCell = self.cellStack[len(self.cellStack)-1]
      self.cellStack = shorten(self.cellStack)
      
      
      

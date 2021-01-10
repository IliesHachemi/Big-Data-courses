class Patch :

    def __init__(self, coord_x, coord_y):
      self.coord_x = coord_x
      self.coord_y = coord_y

    def coord(self) : # Start from bottom left of the 1x1 square
      coord = [(self.coord_x,self.coord_y),
                (self.coord_x,self.coord_y+1),
                (self.coord_x+1,self.coord_y+1),
                (self.coord_x+1,self.coord_y)]
      return coord

class Rectangle: 
    
    def __init__(self, length, width):
        self.length = length
        self.width  = width
        self.idx = -1

    def rectangle_area(self):
        return self.length*self.width

    def rectangle_perimeter(self) :
        return 2*self.length+2*self.width

    n_edges = 4

    @staticmethod
    def talk():
        return "Do you like rectangles?"

    def list_of_patches(self) :
      patches = [] # store patches coordinates
      for i in range(0, self.length):
        for j in range(0, self.width):
          patches.append(Patch(i,j).coord()) # call Patch class coord function
      return patches

    def __iter__(self) : 
      return self

    def __next__(self) : # take care of next or __next__ because of Python 2 / Python 3 incompatibility...
        self.idx += 1
        if self.idx < self.length*self.width :
            self.patch = Rectangle(self.length, self.width).list_of_patches()[self.idx]
            return self.patch
        raise StopIteration

print(Rectangle(2,3).list_of_patches())

for patch in Rectangle(2, 3):
  print(patch)
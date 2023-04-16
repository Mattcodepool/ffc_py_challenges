class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** 0.5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    return ("*"*self.width + "\n")*self.height

  def get_amount_inside(self, shape):
    return (self.width // shape.width) * (self.height // shape.height)
    
  def __str__(self):
    return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
          

class Square(Rectangle):

  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, length):
    self.width = length
    self.height = length

  def __str__(self):
    return "Square(side="+str(self.width)+")"

  def set_width(self, new_width):
    self.width = new_width
    self.height = new_width

  def set_height(self, new_height):
    self.height = new_height
    self.width = new_height

import math

class Point:
  def __init__(self, x, y):
    self.__x = x
    self.__y = y

  @property
  def x(self):
    return self.__x
  @x.setter
  def x(self, x):
    self.__x = x

  @property
  def y(self):
    return self.__y
  @y.setter
  def y(self, y):
    self.__y = y

  def magnitude(self): 
    return math.sqrt(self.x ** 2 + self.y ** 2)

  def subtract(self, point: 'Point'):
    return Point(self.x - point.x, self.y - point.y)

  def distance_to(self, point: 'Point'):
    return self.subtract(point).magnitude()
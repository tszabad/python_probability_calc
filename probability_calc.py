import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k,v in kwargs.items():
      for i in range(v):
        self.contents.append(k)
    print(self.contents)

  def draw(self, num_balls):
    balls = []
    #If the number of balls to draw exceeds the available 
    #quantity, return all the balls.
    if len(self.contents) < num_balls:
      return self.contents
    else:
      for i in range(num_balls):
        picked = random.choice(self.contents)
        balls.append(picked)
        self.contents.pop(self.contents.index(picked))
    return balls
      
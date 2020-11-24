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

    if len(self.contents) < num_balls:
      return self.contents
    else:
      for i in range(num_balls):
        picked = random.choice(self.contents)
        balls.append(picked)
        self.contents.pop(self.contents.index(picked))
    return balls
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  results = 0

  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)

    actual = hat_copy.draw(num_balls_drawn)
    
    actual_dict = {}
    for ball in set(actual):
      actual_dict[ball] = actual.count(ball)


    result = True
    for k, v in expected_balls.items():
      if k not in actual_dict or actual_dict[k] < expected_balls[k]:
        result = False
        break

    if result is True:
      results += 1

  return results/num_experiments
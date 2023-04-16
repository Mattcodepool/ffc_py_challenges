import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    try:
      for key, value in kwargs.items():
        for x in range(0,value):
          self.contents.append(str(key))
    except:
      self.contents.append("grey")
    
    self.pool = copy.deepcopy(self.contents)

  def draw(self, num):
    extracted = []
    self.contents = copy.deepcopy(self.pool)
    if num >= len(self.contents):
      return self.contents
    else:
      for ext in range(0, num):
        idx = random.randint(0,len(self.contents)-1)
        extracted.append(self.contents.pop(idx))
    return extracted

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  N = num_experiments
  expected = []
  for key, value in expected_balls.items():
    for x in range(0,value):
      expected.append(str(key))

  for exp in range(0, int(N)):
    match = 1
    result = hat.draw(num_balls_drawn)
    
    for ball in expected:
      if ball in result:
        result.remove(ball)
      else:
        match = 0
        break
    
    if match == 1:
      M += 1
    
  return M/N
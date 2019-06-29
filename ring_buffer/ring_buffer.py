class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    i = 0
    if len(self.storage) is self.capacity:
      self.storage[:1] = item
    else:
      while self.capacity > i:
        self.storage + [item]


  def get(self):
    for i in self.storage:
      if i is not None:
        print(i)
      else:
        continue
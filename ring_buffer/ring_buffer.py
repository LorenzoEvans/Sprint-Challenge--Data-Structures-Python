class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if len(self.storage) - 1 is self.capacity:
      self.storage[:1] = item
    else:
      self.storage[:0] = item


  def get(self):
    for i in self.storage:
      if i is None:
        continue
      else:
        print(i)
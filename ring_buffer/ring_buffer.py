class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    i = 0
    if i < self.capacity:
      self.storage[:i] = item
    elif i is self.capacity:
      self.storage[:0] = item
    i += 0
    del self.storage[4:len(self.storage) - 1]

  def get(self):
    result = []
    for i in self.storage:
      if i is None:
        continue
      else:
        result.insert(0, i)
    return result
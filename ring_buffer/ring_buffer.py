class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if len(self.storage) is not self.capacity:
      self.storage[:0] = item
    else:
        self.storage[0:] = item


  def get(self):
    for i in self.storage:
      if i is not None:
        print(i)
      else:
        continue
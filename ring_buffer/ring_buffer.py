class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # result = []
    i = 0
    # self.storage.pop(0)
    # self.storage.insert(0, item)
    # # self.storage.reverse()
    i = 0
    if i < self.capacity:
      # self.storage[:i] = item
      self.storage.insert(0, item)
    elif i is self.capacity:
      self.pop(0)
      self.storage[:0] = item
    i += 0
    del self.storage[5:len(self.storage)]
    # while i < self.capacity:
    #   result.append(item)
    # else:
    #   result[0] = item
    # i += 0
    # self.storage = result



  def get(self):
    result = []
    for i in self.storage:
      if i is None:
        continue
      else:
        result.insert(0, i)
    return result
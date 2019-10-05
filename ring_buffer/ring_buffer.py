class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.storage = [None]*capacity

  def append(self, item):
    capacity, storage, current = self.capacity, self.storage, 0
    storage_len = len(self.storage)
    if current < capacity:
      storage.insert(storage_len, item)
      storage_len -= 1
      capacity += 1
    for i in storage:
      if i is None:
        current += 1
        del storage[current]
    # if capacity == storage_len:
    #   storage[0] = item


  def get(self):
    result = []
    for i in self.storage:
      if i is None:
        continue
      else:
        result.insert(0, i)
    return result


testBuffer = RingBuffer(5)

# testBuffer.append('a')
# testBuffer.append('b')
# testBuffer.append('c')
# testBuffer.append('d')
# testBuffer.append('e')
# testBuffer.append('f')

# letters = ['a', 'b', 'c']
# letters[0] = 'i'
# print(letters)
# for i in letters:
#   testBuffer.append(i)

# testBuffer.append('f')

testBuffer.append('a')
testBuffer.append('b')
testBuffer.append('c')
testBuffer.append('d')
testBuffer.append('e')
# testBuffer.append('f')
print(testBuffer.storage)
Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

 ``` python 
 def append(self, item):
    i = 0 
    # This is a primitive operation, so it runs in constant time, or O(1) time.
    if len(self.storage) is self.capacity: 
        # This LOC only runs once to check truthiness/falsiness, so this line runs in constant time or 0(1) time.
      self.storage[:1] = item
        # This LOC only runs once to do variable assignment, so it runs in constant time or O(1) time.
    else:
      while self.capacity > i:
        # This LOC runs n times, where n is the capacity of the buffer/length of the storage, 
          so this runs in linear time, or O(n).
        self.storage + [item]
        # This is a primitive operation, so it runs in constant time or O(1) time.
```

Final runtime complexity of append is O(n), as it's the largest of all the runtimes of any LOC in the function.

2. What is the space complexity of your ring buffer's `append` function?

3. What is the runtime complexity of your ring buffer's `get` method?

4. What is the space complexity of your ring buffer's `get` method?


5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?

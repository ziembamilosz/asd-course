class CircularQueue:

    def __init__(self, size=5):
        self.queue = [None for _ in range(size)]
        self.size = size
        self.write = 0
        self.read = 0

    def __str__(self):
        if self.is_empty():
            return '[]'
        result = '['
        index = self.read
        while index != self.write:
            result += f'{self.queue[index]}, '
            index = (index + 1) % self.size
        return result[0:-2] + ']'

    def get_list(self):
        return self.queue

    def is_empty(self):
        return bool(self.write == self.read)

    def peek(self):
        return self.queue[self.read]

    def realloc(self):
        old_size = self.size
        self.size = 2 * self.size
        self.queue = [self.queue[x] if x < self.write else
                      (self.queue[x-old_size] if x > old_size else None) for x in range(self.size)]
        self.read += old_size

    def dequeue(self):
        if self.is_empty():
            return None
        result = self.queue[self.read]
        self.queue[self.read] = None
        self.read = (self.read + 1) % self.size
        return result

    def enqueue(self, entry):
        self.queue[self.write] = entry
        self.write = (self.write + 1) % self.size
        if self.write == self.read:
            self.realloc()


queue = CircularQueue()
for i in range(1, 5):
    queue.enqueue(i)
print(queue.dequeue())
print(queue.peek())
print(queue)
for i in range(5, 9):
    queue.enqueue(i)
print(queue.get_list())
while not queue.is_empty():
    queue.dequeue()
print(queue)

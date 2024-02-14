class MyQueue:

    def __init__(self):
        self.queue = []
        self.size = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.size > 0:
            self.size -= 1
            return self.queue.pop(0)
        return -1

    def peek(self) -> int:
        if self.size > 0:
            return self.queue[0]
        return -1
    def empty(self) -> bool:
        return self.size == 0
        

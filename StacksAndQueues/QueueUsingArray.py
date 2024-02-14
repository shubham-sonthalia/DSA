class Queue:
    def __init__(self):
        self.queue = []
        self.curSize = 0
    
    #  Enqueue (add) element 'e' at the end of the queue.
    def enqueue(self, e: int) -> None:
        self.queue.append(e)
        self.curSize += 1
        # Write your code here.
        pass

    #  Dequeue (retrieve) the element from the front of the queue.
    def dequeue(self) -> int:
        if self.curSize > 0:
            self.curSize -= 1
            return self.queue.pop(0)
        else:
            return -1
        # Write your code here.
        pass

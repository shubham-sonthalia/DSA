class MyStack:
    def __init__(self):
        self.queue = []
    def push(self, x: int) -> None:
        self.queue.append(x)       

    def pop(self) -> int:
        if len(self.queue)  == 0: 
            return -1
        return self.queue.pop(-1)

    def top(self) -> int:
        if len(self.queue)  == 0: 
            return -1
        return self.queue[-1]

    def empty(self) -> bool:
        if len(self.queue) == 0: 
            return True
        return False

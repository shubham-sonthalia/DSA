class Stack:
    def __init__(self, n: int):
        self.capacity = n
        self.curSize = 0 
        self.stack = [] 
        # Write your code here
        pass

    def push(self, num: int):
        if self.curSize < self.capacity:
            self.curSize += 1
            self.stack.append(num)
        # Write your code here

        pass

    def pop(self) -> int:
        # Write your code here
        if self.curSize > 0:
            self.curSize -= 1
            return self.stack.pop()
        else:
            return -1
        pass

    def top(self) -> int:
        # Write your code here
        if self.curSize > 0:
            return self.stack[-1]
        else:
            return -1
        pass

    def isEmpty(self) -> int:
        if self.curSize == 0:
            return 1
        return 0
        # Write your code here
        pass

    def isFull(self) -> int:
        if self.curSize == self.capacity:
            return 1
        return 0
        # Write your code here
        pass

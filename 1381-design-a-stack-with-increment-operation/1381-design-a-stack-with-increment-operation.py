class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.size = 0
        self.ops = []
        self.stack = []
        

    def push(self, x: int) -> None:
        if self.size == self.max_size:
            return
        self.size += 1
        self.stack.append(x)
        
    def pop(self) -> int:
        if self.size == 0:
            return -1
        new_ops = []
        ret = self.stack.pop()
        for (start, end, val) in self.ops:
            if end >= self.size - 1:
                ret += val
                new_ops.append((start, self.size - 2, val))
                continue
            new_ops.append((start, end, val))
        self.ops = new_ops
        self.size -= 1
        return ret
            
    def increment(self, k: int, val: int) -> None:
        if self.size == 0:
            return
        self.ops.append((0,min(self.size-1, k-1),val))

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.heap, val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.heap = self.stack[:]
        heapq.heapify(self.heap)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        if self.heap:
            return self.heap[0]

        

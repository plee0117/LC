class MinStack():

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = list()
        
    def push(self, x: int) -> None:
        if self.items == []:
            self.items.append((x,x))
        else:
            self.items.append((x,min(x,self.items[-1][1])))

    def pop(self) -> None:
        self.items.pop()
        
    def top(self) -> int:
        return self.items[-1][0]

    def getMin(self) -> int:
        return self.items[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
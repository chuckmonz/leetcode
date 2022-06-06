class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minValues = []
        self.minValue = None
        pass

    def push(self, val: int):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        
        if self.minValue is not None:       
            self.minValue = min(self.minValue, val)
        else:
            self.minValue = val
        self.minValues.append(self.minValue)
        pass
        

    def pop(self):
        self.minValues.pop()
        self.minValue = self.minValues[-1]
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minValue
        


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) ## return -3
minStack.pop()
print(minStack.top()) ## return 0
print(minStack.getMin()) ## return -2
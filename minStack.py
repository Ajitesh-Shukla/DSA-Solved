'''If we just take the min element with us, how will we get the next min elem when it is popped
Do it at the expense of space complexity
Store another array that only stores the next smaller elem
If an element after another elem is greater, its of no use to us for min elem determination'''

class MinStack:

    def __init__(self):
        self.stack=[]
        self.stackmin=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (self.stackmin and val<=self.stackmin[-1]) or not self.stackmin:
            self.stackmin.append(val)

    def pop(self) -> None:
        popped_elem=self.stack.pop(-1)
        if self.stackmin and popped_elem==self.stackmin[-1]:
            self.stackmin.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.stackmin:
            return self.stackmin[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(0)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)
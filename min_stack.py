#Design a stack class that supports the push, pop, top, and getMin operations.
#MinStack() initializes the stack object.
#void push(int val) pushes the element val onto the stack.
#void pop() removes the element on the top of the stack.
#int top() gets the top element of the stack.
#int getMin() retrieves the minimum element in the stack.
#Each function should run in O(1) time.
class MinStack:

    def __init__(self):
        self.stack = []
        self.extra = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.extra:
            self.extra.append(val)
        else:
            self.extra.append(min(self.extra[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.extra.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.extra[-1]

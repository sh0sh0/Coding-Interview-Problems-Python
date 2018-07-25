### leetcode 155
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, x):
        self.stack.append(x)
        if len(self.minstack) and x == self.minstack[-1][0]:
            self.minstack[-1][1] += 1
        elif len(self.minstack)== 0 or x < self.minstack[-1][0]:
            self.minstack.append([x,1])

    def pop(self):
        if self.top() == self.getMin():
            if self.minstack[-1][1] > 1:
                self.minstack[-1][1] -= 1
            else:
                self.minstack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minstack[-1][0]

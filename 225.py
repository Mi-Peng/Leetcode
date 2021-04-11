# method1. use one queue:
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)

        for t in range(len(self.q) - 1):
            head = self.q.pop(0)
            self.q.append(head)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        result = self.q.pop(0)
        return result

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0
# method2. use two queue:
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q2.append(x)
        for i in range(len(self.q1)):
            num = self.q1.pop(0)
            self.q2.append(num)
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        result = self.q1.pop(0)
        return result

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
'''Design a data structure, which represents two stacks using only one array common for both stacks. The data structure should support the following operations:

push1(NUM) - Push ‘NUM’ into stack1.
push2(NUM) - Push ‘NUM’ into stack2.
pop1() - Pop out a top element from stack1 and return popped element, in case of underflow return -1.
pop2() - Pop out a top element from stack2 and return popped element, in case of underflow return -1.
There are 2 types of queries in the input

Type 1 - These queries correspond to Push operation.
Type 2 - These queries correspond to Pop operation.
Note:

1. You are given the size of the array.

2. You need to perform push and pop operations in such a way that we are able to push elements in the stack until there is some empty space available in the array.

3. While performing Push operations, do nothing in the situation of the overflow of the stack
'''

class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = n

    # Method to push an element into stack1
    def push1(self, num):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = num

    # Method to push an element into stack2
    def push2(self, num):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = num

    # Method to pop an element from stack1
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            return -1  # Stack underflow

    # Method to pop an element from stack2
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            return -1  # Stack underflow

# Example usage
if __name__ == "__main__":
    ts = TwoStacks(5)
    ts.push1(5)
    ts.push2(10)
    ts.push1(15)
    ts.push2(20)
    ts.push1(25)

    print("Popped from stack1:", ts.pop1())
    print("Popped from stack2:", ts.pop2())

/* Design a data structure, which represents two stacks using only one array common for both stacks. The data structure should support the following operations:

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
  */

public class TwoStacks {
    int[] arr;
    int size;
    int top1, top2;

    // Constructor
    public TwoStacks(int n) {
        size = n;
        arr = new int[n];
        top1 = -1;
        top2 = n;
    }

    // Method to push an element into stack1
    public void push1(int num) {
        if (top1 < top2 - 1) {
            arr[++top1] = num;
        }
    }

    // Method to push an element into stack2
    public void push2(int num) {
        if (top1 < top2 - 1) {
            arr[--top2] = num;
        }
    }

    // Method to pop an element from stack1
    public int pop1() {
        if (top1 >= 0) {
            return arr[top1--];
        } else {
            return -1; // Stack underflow
        }
    }

    // Method to pop an element from stack2
    public int pop2() {
        if (top2 < size) {
            return arr[top2++];
        } else {
            return -1; // Stack underflow
        }
    }

    // Driver code
    public static void main(String[] args) {
        TwoStacks ts = new TwoStacks(5);
        ts.push1(5);
        ts.push2(10);
        ts.push1(15);
        ts.push2(20);
        ts.push1(25);

        System.out.println("Popped from stack1: " + ts.pop1());
        System.out.println("Popped from stack2: " + ts.pop2());
    }
}


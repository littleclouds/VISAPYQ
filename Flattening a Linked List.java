// Given a Linked List, where every node represents a sub-linked-list and contains two pointers:
// (i) a next pointer to the next node,
// (ii) a bottom pointer to a linked list where this node is head.
// Each of the sub-linked lists is in sorted order.
// Flatten the Link List so all the nodes appear in a single level while maintaining the sorted order.
// Note: The flattened list will be printed using the bottom pointer instead of the next pointer. Look at the printList() function in the driver code for more clarity.
// Expected Time Complexity: O(n * n * m)
// Expected Auxiliary Space: O(n)
// Constraints:
// 0 <= number of nodes <= 50
// 1 <= no. of nodes in sub-LinkesList(mi) <= 20
// 1 <= node->data <= 103

// User function Template for Java

 class Solution {
    // Flatten the multi-level list
    public Node flatten(Node root) {
        if (root == null) {
            return null;
        }

        // Min-heap to maintain the sorted order while merging
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> a.data - b.data);

        // Push all the nodes of the first level into the priority queue
        Node current = root;
        while (current != null) {
            pq.offer(current);
            current = current.next;
        }

        // Dummy node to start the flattened list
        Node dummy = new Node(0);
        Node tail = dummy;

        // Process the priority queue to build the flattened list
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            tail.bottom = node;
            tail = tail.bottom;

            // If the node has a bottom list, add it to the queue
            if (node.bottom != null) {
                pq.offer(node.bottom);
            }

            // Remove the next pointer for flattened list
            node.next = null;
        }

        return dummy.bottom;
    }
}

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
/* Given a singly linked list. The task is to remove duplicates (nodes with duplicate values) from the given list (if it exists). 
1 <= Number of nodes, data of nodes <= 105 */

class Node {
    int data;
    Node next;
    Node(int x) {
        data = x;
        next = null;
    }
}

class Solution {
    // Function to remove duplicates from sorted linked list.
    Node removeDuplicates(Node head) {
        // If the list is empty or has only one node, return the head
        if (head == null || head.next == null) {
            return head;
        }

        // Initialize current node
        Node current = head;

        // Traverse the list
        while (current != null && current.next != null) {
            // If current node's data is equal to next node's data
            if (current.data == current.next.data) {
                // Skip the next node
                current.next = current.next.next;
            } else {
                // Move to the next node
                current = current.next;
            }
        }

        return head;
    }
}

/* You are given an unsorted Singly Linked List with 'N' nodes which may contain duplicate elements. You are supposed to remove all duplicate elements from the linked list and keep only the last appearance of elements.
*/

import java.util.HashMap;

class Node {
    int data;
    Node next;
    Node(int x) {
        data = x;
        next = null;
    }
}

public class RemoveDuplicates {
    public Node removeDuplicates(Node head) {
        if (head == null) {
            return null;
        }

        HashMap<Integer, Node> map = new HashMap<>();
        Node current = head;
        Node prev = null;

        while (current != null) {
            if (map.containsKey(current.data)) {
                prev.next = current.next;
            } else {
                map.put(current.data, current);
                prev = current;
            }
            current = current.next;
        }

        return head;
    }

    // Helper function to print the linked list
    public void printList(Node head) {
        while (head != null) {
            System.out.print(head.data + " -> ");
            head = head.next;
        }
        System.out.println("null");
    }

    // Driver code
    public static void main(String[] args) {
        RemoveDuplicates solution = new RemoveDuplicates();
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(2);
        head.next.next.next = new Node(3);
        head.next.next.next.next = new Node(4);
        head.next.next.next.next.next = new Node(3);

        System.out.println("Original list:");
        solution.printList(head);

        head = solution.removeDuplicates(head);

        System.out.println("List after removing duplicates:");
        solution.printList(head);
    }
}

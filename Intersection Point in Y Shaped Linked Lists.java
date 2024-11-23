/* Given two singly linked lists, write a program to get the point where two linked lists intersect each other. 
If the linked list does not merge at any point, it should return -1. */


/* 
Node of a linked list
class Node {
    int data;
    Node next;
    Node(int d) {
        data = d;
        next = null;
    }
}

Linked List class
class LinkedList {
    Node head; // head of list
}
*/

class Solution {
    Node intersectPoint(Node head1, Node head2) {
        // Write your code here
        // Base Condition
        if (head1 == null || head2 == null) {
            return null;
        }
        Node temp1 = head1;
        Node temp2 = head2;
        while (temp1 != temp2) {
            temp1 = temp1.next;
            temp2 = temp2.next;
            if (temp1 == temp2) {
                return temp1;
            }
            if (temp1 == null) {
                temp1 = head2;
            }
            if (temp2 == null) {
                temp2 = head1;
            }
        }
        return temp1;
    }
}

/*
Given two singly linked lists, return the point where two linked lists intersect.
2 ≤ size of first linkedist + size of second linkedlist ≤ 2*105
-10000 ≤ data of nodes ≤ 10000 */

class Intersect {
    // Function to find intersection point in Y shaped Linked Lists.
    int intersectPoint(Node head1, Node head2) {
        // code here
        int n1=size(head1);
        int n2=size(head2);
        while(n1>n2){
            head1=head1.next;
            n1--;
        }
        while(n2>n1){
            head2=head2.next;
            n2--;
        }
        while(head1!=null&&head2!=null){
            if(head1==head2){
                return head1.data;
            }
            head1=head1.next;
            head2=head2.next;
        }
        return -1;
    }
    public static int size(Node head){
        Node temp=head;
        int c=0;
        while(temp!=null){
            c++;
            temp=temp.next;
            
        }
        return c;
    }
}

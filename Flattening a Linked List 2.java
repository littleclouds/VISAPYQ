/* Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
Note: The flattened list will be printed using the bottom pointer instead of next pointer.*/

/*Node class  used in the program
class Node
{
	int data;
	Node next;
	Node bottom;
	
	Node(int d)
	{
		data = d;
		next = null;
		bottom = null;
	}
}
*/
/*  Function which returns the  root of 
    the flattened linked list. */
class GfG
{
    Node flatten(Node root)
    {
   Node temp = root;
      
      ArrayList<Integer> li = new ArrayList();
     
      Node dummy = new Node(-1);
      while(temp!=null){
           Node curr = temp;
           while(curr!=null){
              li.add(curr.data); 
              curr = curr.bottom;
           }
           temp = temp.next;
           
      }
      
      Collections.sort(li);
      Node curr = dummy;
      for(int i = 0;i<li.size();i++){
          Node ne = new Node(li.get(i));
          curr.bottom = ne;
          curr = curr.bottom;
      }
    
    return dummy.bottom;
    }
}

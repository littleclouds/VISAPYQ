/* You have been given a Binary Tree of 'n' nodes, where the nodes have integer values. Your task is to return the In-Order traversal of the given binary tree*/

import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int item) {
        val = item;
        left = right = null;
    }
}

public class BinaryTree {
    TreeNode root;

    // Function to perform In-Order traversal
    public List<Integer> inOrderTraversal(TreeNode node) {
        List<Integer> result = new ArrayList<>();
        inOrderHelper(node, result);
        return result;
    }

    private void inOrderHelper(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        inOrderHelper(node.left, result);
        result.add(node.val);
        inOrderHelper(node.right, result);
    }

    // Driver code
    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();
        tree.root = new TreeNode(1);
        tree.root.left = new TreeNode(2);
        tree.root.right = new TreeNode(3);
        tree.root.left.left = new TreeNode(4);
        tree.root.left.right = new TreeNode(5);

        List<Integer> inOrder = tree.inOrderTraversal(tree.root);
        System.out.println("In-Order Traversal: " + inOrder);
    }
}

// import java.util.ArrayList;
// import java.util.LinkedList;
// import java.util.List;
// import java.util.Queue;

// import javax.swing.tree.TreeNode;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
// class Solution {
// public List<List<Integer>> levelOrder(TreeNode root) {
// List<List<Integer>> res = new ArrayList();
// if (root == null) {return res;}

// Queue<TreeNode> queue = new LinkedList();
// queue.add(root);

// while (queue.size() > 0){
// int size = queue.size();
// List<Integer> tmp = new ArrayList();
// for(int i=0; i< size; i++){
// TreeNode current = queue.poll();
// tmp.add(current.val);
// if(current.left!=null){
// queue.add(current.left);
// }
// if(current.right!=null){
// queue.add(current.right);
// }
// }
// res.add(tmp);
// }

// return res;
// }
// }
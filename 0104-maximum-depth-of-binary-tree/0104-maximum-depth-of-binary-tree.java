/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        int add = 0;
        Queue<TreeNode> temp = new LinkedList<>();
        temp.offer(root);
        while(!temp.isEmpty()){
            
            int size = temp.size();
            for(int i = 0 ; i < size ;i++){
                TreeNode item = temp.poll();
                if(item.left != null) temp.offer(item.left);
                if(item.right != null) temp.offer(item.right);
            }
            add++;
        }
        return add;
    }
}
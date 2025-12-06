# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # First, a helper that returns (lca_node, found_p, found_q)
        def helper(node):
            if not node:
                return (None, False, False)
            
            left_lca, left_p, left_q = helper(node.left)
            right_lca, right_p, right_q = helper(node.right)
            
            found_p = left_p or right_p or (node is p)
            found_q = left_q or right_q or (node is q)
            
            # If this node is p or q:
            if node is p or node is q:
                return (node, found_p, found_q)
            
            # If p and q are found in different subtrees => this node is LCA
            if left_lca and right_lca:
                return (node, found_p, found_q)
            if left_lca:
                return (left_lca, found_p, found_q)
            if right_lca:
                return (right_lca, found_p, found_q)
            
            # Otherwise no LCA found here
            return (None, found_p, found_q)
        
        lca, found_p, found_q = helper(root)
        # Only return lca if both p and q exist in tree
        return lca if (found_p and found_q) else None

  
# Leetcode 1038. Binary Search Tree to Greater Sum Tree

# Runtime: O(N) 28 ms, faster than 75.20% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
# Memory Usage: O(1) 12.8 MB, less than 100.00% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.current_sum = 0
    
        # a traversal of the tree (preorder traversal?)
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            self.current_sum += node.val
            node.val = self.current_sum
            dfs(node.left)
        
        dfs(root)
        return root
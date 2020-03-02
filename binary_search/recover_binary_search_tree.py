# Leetcode 99. Recover Binary Search Tree


# Solution 1 Sort an almost sorted array where two elements are swapped
# Runtime: O(N)
# Memory Usage: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def inorder_traversal(node: TreeNode) -> List[int]:
        	if not root:
        		return []

        	return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

        def find_two_swapped(nums: List[int]) -> (int, int):
        	n = len(nums)
        	x = y = -1
        	for i in range(n-1):
        		if nums[i+1] < nums[i]:
        			y = nums[i+1]
        			# first swap occurence
        			if x == -1:
        				x = nums[i]
        			# second swap occurence
        			else:
        				break
        	return x, y

        def recover(root: TreeNode, count: int):
        	if r:
        		if r.val == x or r.val == y:
        			if r.val == x:
        				r.val = y
        			else:
        				r.val = x

        			count -= 1

        			if count == 0:
        				return

        		recover(r.left, count)
        		recover(r.right, count)

        nums = inorder(root)
        x, y = find_two_swapped(nums)
        recover(root, 2)

# Solution 2: Iterative inorder traversal
# Runtime: O(1) best case, O(N) worst case
# Memory Usage: O(H) to keep the stack where H is the tree height

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = [] # stack helps us keep the record of parent nodes that are larger than current node
        x = y = pred = None # pred: previous number in the sorted array

        while stack or root: # when traversing the tree either stack or root must not be null
        	while root:
        		stack.append(root)
        		root = root.left # visit left child first
        		
        		# first swap occurence
        		if pred and root.val < pred.val
        			y = root
        			if x is None:
        				x = pred
        			# second swap occurence
        			else:
        				break

        		pred = root
        		root = root.right

        # swap two values
        x.val, y.val = y.val, x.val






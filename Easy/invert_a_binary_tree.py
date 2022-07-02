'''
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Solution 1: Recursion
        if not root or (not root.left and not root.right):
            return root
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            
            tmp = root.left
            root.left = root.right
            root.right = tmp
            
        return root
    
    
    '''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Solution 2: Iterative
        if not root:
            return root
        
        queue = collections.deque([root])
        
        while queue:
            cur = queue.popleft()
            tmp = cur.left
            cur.left = cur.right
            cur.right = tmp
            
            if tmp:
                queue.append(tmp)
            if cur.left:
                queue.append(cur.left)
        
        return root
    '''
    
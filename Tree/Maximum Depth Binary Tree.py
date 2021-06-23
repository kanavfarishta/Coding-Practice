#Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root == None):
            return(0)
        else:
            return(self.recursiveFunction(root,1))
    
    def recursiveFunction(self,node,count):
        count1 = count
        count2 = count 
        if(not node.left == None):
            count1 = self.recursiveFunction(node.left,count+1)
        if(not node.right == None):
            count2 = self.recursiveFunction(node.right,count+1)
        return(max(count1,count2))

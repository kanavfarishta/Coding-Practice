#Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if(root == None):
            return(False)
        else:
            return(self.recursiveFunction(root,0,targetSum))
    
    def recursiveFunction(self,node,sums,targetSum):
        if(node.left == None and node.right == None):
            if(sums + node.val== targetSum):
                return(True)
            else:
                return(False)
        if(not node.left == None):
            op = self.recursiveFunction(node.left,sums+node.val,targetSum)
            if(op):
                return(op)
            
        if(not node.right == None):
            op = self.recursiveFunction(node.right,sums+node.val,targetSum)
            if(op):
                return(op)
            
        return(False) 

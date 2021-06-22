#Binary Tree Inorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if(root == None):
            return([])
        else:
            return(self.recursiveFunction(root,[]))
    
    def recursiveFunction(self,node,List):
        if(not node.left == None):
            List = self.recursiveFunction(node.left,List)
        List.append(node.val)
        if(not node.right == None):
            List = self.recursiveFunction(node.right,List)
        return(List)

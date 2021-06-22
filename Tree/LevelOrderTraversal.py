#Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if(root == None):
            return([])
        else:
            op = self.recursiveFunction(root,{},0)
            return([op[i] for i in op])
    
    def recursiveFunction(self,node,List,level):
        try:
            List[level].append(node.val)
            #print(level,node.val)
        except:
            #print(level,node.val)
            List[level] = [node.val]
        if(not node.left == None):
            List = self.recursiveFunction(node.left,List,level+1)
            #print('L',List)
        if(not node.right == None):
            List = self.recursiveFunction(node.right,List,level+1)
            #print('R',List)
        return(List) 

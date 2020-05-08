'''
Cousins in Binary Tree
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.


solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xval=[]
        yval=[]
        dep=0
        par=None
        if root is None:
            return False

        self.sfd(root,x,y,0,None,xval,yval)
        return xval[0][0]==yval[0][0] and xval[0][1]!=yval[0][1]

    def sfd(self,root,x,y,dep,par,xval,yval):
        if root is None:
            return None
        if root.val==x:
            xval.append((dep,par))
        if root.val==y:
            yval.append((dep,par))

        self.sfd(root.left,x,y,dep+1,root,xval,yval)
        self.sfd(root.right,x,y,dep+1,root,xval,yval)
        


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder)
        return self.bstfrompreandin(preorder, inorder)

    def bstfrompreandin(self, preorder, inorder):
        lenin = len(inorder)
        lenpre = len(preorder)
        if lenpre != lenin or lenpre == 0 or preorder == None or inorder == None:
            return None
        root = TreeNode(preorder[0])
        rootindex = inorder.index(root.val)
        root.left = self.bstfrompreandin(preorder[1:rootindex + 1], inorder[:rootindex])
        root.right = self.bstfrompreandin(preorder[rootindex + 1:], inorder[rootindex + 1:])
        return root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None


if __name__ == '__main__':
    nodeList = []
    for i in range(9):
        node = TreeNode(i)
        nodeList.append(node)
    nodeList[3].left = nodeList[5]
    nodeList[3].right = nodeList[1]
    nodeList[5].left = nodeList[6]
    nodeList[5].right = nodeList[2]
    nodeList[1].left = nodeList[0]
    nodeList[1].right = nodeList[8]
    root = nodeList[3]
    sol = Solution()
    print(sol.lowestCommonAncestor(root, nodeList[4], nodeList[5]).val)

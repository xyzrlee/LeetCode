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
        if p.val > q.val:
            p, q = q, p
        if not root or root.val == p.val or root.val == q.val:
            return root
        if root.val > p.val and root.val < q.val:
            return root
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return None


if __name__ == '__main__':
    nodeList = []
    for i in range(10):
        node = TreeNode(i)
        nodeList.append(node)
    nodeList[6].left = nodeList[2]
    nodeList[6].right = nodeList[8]
    nodeList[2].left = nodeList[0]
    nodeList[2].right = nodeList[4]
    nodeList[4].left = nodeList[3]
    nodeList[4].right = nodeList[5]
    nodeList[8].left = nodeList[7]
    nodeList[8].right = nodeList[9]
    root = nodeList[6]
    sol = Solution()
    print(sol.lowestCommonAncestor(root, nodeList[2], nodeList[8]).val)

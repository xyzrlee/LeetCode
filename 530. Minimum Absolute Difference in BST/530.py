# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def inOrderTraverse(root):
            if root is None:
                return []
            return inOrderTraverse(root.left) + [root.val] + inOrderTraverse(root.right)

        inOrderList = inOrderTraverse(root)
        if len(inOrderList) < 2:
            return 0
        min = abs(inOrderList[-1] - inOrderList[0])
        for i in range(len(inOrderList) - 1):
            x = abs(inOrderList[i + 1] - inOrderList[i])
            if x < min:
                min = x
        return min


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
    print(sol.getMinimumDifference(root))

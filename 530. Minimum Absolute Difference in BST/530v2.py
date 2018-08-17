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

        last, min = None, None

        def dfs(root):
            nonlocal last, min
            if root is None:
                return
            dfs(root.left)
            if last is not None:
                x = abs(root.val - last)
                if min is None or min > x:
                    min = x
            last = root.val
            dfs(root.right)

        dfs(root)
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

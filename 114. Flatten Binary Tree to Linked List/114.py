# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "%r l:[%r] r:[%r]" % (self.val, self.left, self.right)


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        r = TreeNode(None)
        s = [root]
        while s:
            n = s.pop()
            r.left = None
            r.right = n
            if n and n.right:
                s.append(n.right)
            if n and n.left:
                s.append(n.left)
            r = n


if __name__ == '__main__':
    sol = Solution()
    n = []
    for i in range(8):
        n.append(TreeNode(i))
    n[1].left = n[2]
    n[1].right = n[5]
    n[2].left = n[3]
    n[2].right = n[4]
    n[5].right = n[6]
    print("%r" % n[1])
    sol.flatten(n[1])
    print("%r" % n[1])

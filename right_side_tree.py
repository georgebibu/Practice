#You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        while q:
            right_element = None
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if node:
                    right_element = node
                    q.append(node.left)
                    q.append(node.right)
            if right_element:
                res.append(right_element.val)
        return res

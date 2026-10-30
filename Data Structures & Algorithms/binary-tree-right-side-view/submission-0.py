# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

LEFT = 0
RIGHT = 1

def compareDepths(d1, d2):
    for i in range(min(len(d1), len(d2))):
        if d1[i] > d2[i]:
            return 1
        if d1[i] < d2[i]:
            return -1
    return 0

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        stack = [(root, [])]
        nodes = []
        while stack:
            node, depth = stack.pop()
            if not node: continue
            if len(depth) >= len(nodes):
                nodes.append((node.val, depth))
            else:
                if compareDepths(depth, nodes[len(depth)-1][1]) == 1:
                    nodes[len(depth)-1] = (node.val, depth)
            stack.append((node.left, depth + [LEFT]))
            stack.append((node.right, depth + [RIGHT]))
        ans = [t[0] for t in nodes]
        return ans
        
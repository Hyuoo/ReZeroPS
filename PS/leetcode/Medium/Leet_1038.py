"""
Solving Date    : 2024.06.25
Solving Time    : 13m
Title           : 1038. Binary Search Tree to Greater Sum Tree
tags            : binary_tree, BST
url             : https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
runtime         : 26 ms
memory          : 16.5 MB
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    tot = 0
    
    def rev_order_trv(self, node: TreeNode) -> None:
        if node is None:
            return
        self.rev_order_trv(node.right)
        self.tot += node.val
        node.val = self.tot
        self.rev_order_trv(node.left)
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.rev_order_trv(root)
        return root
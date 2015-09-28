# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:48:39 2015

@author: congxiu
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#class Solution:
#    # @param {integer[]} preorder
#    # @param {integer[]} inorder
#    # @return {TreeNode}
#    def buildTree(self, preorder, inorder):
#        def connect(node, p_list_idx, i_list_idx):
#            p_list = preorder[p_list_idx[0]:p_list_idx[1]]
#            i_list = inorder[i_list_idx[0]:i_list_idx[1]]
#            mid_i_idx = i_list.index(p_list[0])
#            if mid_i_idx >= 1:
#                left = TreeNode(p_list[1])
##                node_list.append(left)
#                node.left = left
#                connect(left, [p_list_idx[0] + 1, p_list_idx[0] + mid_i_idx + 1], 
#                        [i_list_idx[0], i_list_idx[0] + mid_i_idx])
#            if len(p_list) - mid_i_idx >= 2:
#                right = TreeNode(p_list[mid_i_idx + 1])
##                node_list.append(right)
#                node.right = right
#                connect(right, [p_list_idx[0] + mid_i_idx + 1, p_list_idx[1]],
#                        [i_list_idx[0] + mid_i_idx + 1, i_list_idx[1]])
#                        
#            return True
#            
#        if preorder:
##            node_list = []
##            node_list.append(TreeNode(preorder[0]))
#            n = TreeNode(preorder[0])
#            connect(n, [0, len(preorder)], [0, len(inorder)])
#            return n
##            connect(node_list[0], [0, len(preorder)], [0, len(inorder)])
#            
##            return node_list[0]
#        else:
#            return None
            
            
class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        def connect(node, p_list_idx, i_list_idx):
            p_list = preorder[p_list_idx[0]:p_list_idx[1]]
            i_list = inorder[i_list_idx[0]:i_list_idx[1]]
            mid_i_idx = i_list.index(p_list[0])
            if mid_i_idx >= 1:
                left = TreeNode(p_list[1])
                node.left = left
                left_sub_tree = (left, [p_list_idx[0] + 1, p_list_idx[0] + mid_i_idx + 1], 
                                 [i_list_idx[0], i_list_idx[0] + mid_i_idx])
            else:
                left_sub_tree = None
                
            if len(p_list) - mid_i_idx >= 2:
                right = TreeNode(p_list[mid_i_idx + 1])
                node.right = right
                right_sub_tree = (right, [p_list_idx[0] + mid_i_idx + 1, p_list_idx[1]],
                        [i_list_idx[0] + mid_i_idx + 1, i_list_idx[1]])
            else:
                right_sub_tree = None
                        
            return [left_sub_tree, right_sub_tree]
            
        if preorder:
            q = []
            n = TreeNode(preorder[0])
            q.append((n, [0, len(preorder)], [0, len(inorder)]))
            left, right = connect(*q[0])
            while q:
                left, right = connect(*q.pop(0))
                if left:
                    q.append(left)
                if right:
                    q.append(right)
                    
            return n
        else:
            return None
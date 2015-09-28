# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:43:22 2015

@author: congxiu
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        curr_node = head
        node_list = set([])
        l = 0
        while curr_node:
            l = l + 1
            node_list.update([curr_node])
            if l != len(node_list):
                return True
                
            curr_node = curr_node.next
                
        return False
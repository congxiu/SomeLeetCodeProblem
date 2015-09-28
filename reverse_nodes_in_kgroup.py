# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:38:59 2015

@author: westlake3
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        def exchangenode(node1, node2):
            next_node = node2.next
            node2.next = node1
            
            return next_node
        
        def one_loop(head, k):
            curr_node = head
            next_node = curr_node.next
            counter = 1
            
            while counter < k:
                counter += 1
                temp = exchangenode(curr_node, next_node)
                curr_node = next_node
                next_node = temp
                
            return [curr_node, next_node]
        
        if not head:
            return head
        
        if k == 1:
            return head
            
        temp = head
        counter = 1
        while temp.next:
            counter += 1
            temp = temp.next
            
        size = counter / k
        if size < 1:
            return head
        
        loop_counter = 1
        first_node, next_node = one_loop(head, k)
        last_head = head
        while loop_counter < size:
            this_head = next_node
            curr_node, next_node = one_loop(next_node, k)
            last_head.next = curr_node
            last_head = this_head
            
            loop_counter += 1


        last_head.next = next_node
        return first_node


node_list = [ListNode(x) for x in range(1, 6)]
for idx, x in enumerate(node_list[:-1]):
    x.next = node_list[idx + 1]
    
for x in node_list:
    print x.val
    
for x in node_list:
    if x.next:
        print x.next.val
    else:
        print "None!"

s = Solution()
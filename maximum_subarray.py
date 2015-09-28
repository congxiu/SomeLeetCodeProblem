# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:09:26 2015

@author: congxiu
"""
a = [2, 1, -3, 4, -1, 2, 1, -5, 4]

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        boundry = []
        current_node = 0
        sums = 0
        
        for idx, num in enumerate(nums):
            if num < 0:
                right_extension = sums + num > 0
                boundry.append([current_node, idx, sums, right_extension])
                current_node = idx
                sums = 0
            else:
                sums += num
                
        boundry.append([current_node, len(nums), sums, True])
        boundry[0].append(True)
        
        for a_boundry in boundry[1:]:
            a_boundry.append(a_boundry[2] + nums[a_boundry[0]] > 0)
        
        print boundry
#        for idx, left_b in enumerate(boundry[:-1]):
            
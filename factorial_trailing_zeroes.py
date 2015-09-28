# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:32:02 2015

@author: westlake3
"""

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        n = abs(n)
        c = 0
        while n >= 5:
            n = n / 5
            c = c + n
        
        return c
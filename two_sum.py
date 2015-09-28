# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:29:53 2015

@author: westlake3
"""

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        half = target / 2
        less = {}
        more = {}
        equal = []
        for idx, x in enumerate(num):
            if x > half:
                more[x] = idx
            elif x < half:
                less[x] = idx
            else:
                equal.append(idx)
                
        if len(equal) == 2:
            return(equal[0] + 1, equal[1] + 1)
            
        if len(more) > len(less):
            for x in less:
                value = target - x
                if value in more:
                    idx1 = more[value] + 1
                    idx2 = less[x] + 1
                    if idx1 > idx2:
                        return (idx2, idx1)
                    else:
                        return (idx1, idx2)
        else:
            for x in more:
                value = target - x
                if value in less:
                    idx1 = less[value] + 1
                    idx2 = more[x] + 1
                    if idx1 > idx2:
                        return (idx2, idx1)
                    else:
                        return (idx1, idx2)
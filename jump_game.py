# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:42:01 2015

@author: westlake3
"""
import timeit
start = timeit.default_timer()
###############Recursive and got stack overflow as a result...
#class Solution:
#    # @param nums, an integer[]
#    # @return a boolean
#    def canJump(self, nums):
#        def cal_canJump(st, ed):
#            if (st, ed) in table:
#                return table[(st, ed)]
#            else:
#                reach = min(ed - st, nums[st])
#                
#                for n in range(reach, 0, -1):
#                    table[(st, st + n)] = True
#                    if (st + n, ed) not in table:
#                        table[(st + n, ed)] = cal_canJump(st + n, ed)
#                    if table[(st + n, ed)]:  
#                        table[(st, ed)] = True
#                        return True
#                    
#            table[(st, ed)] = False
#            return False
#                        
#                        
#        if not nums:
#            return False
#            
#        size = len(nums)
#        table = {(n , n) : True for n in range(size)}
#        return  cal_canJump(0, size - 1)
        
        
###############Non recursive using DFS, timed out...
class Solution:
    # @param nums, an integer[]
    # @return a boolean
    def canJump(self, nums):
        last = len(nums) -1
        checked = []
        Q = [0]
        
        while Q:
            if Q[-1] >= last:
                return True
                
            curr = Q.pop(-1)
            checked.append(curr)
            for step in range(1, nums[curr] + 1):
                if curr + step not in checked:
                    Q.append(curr + step)
                
        return False
        
s = Solution()
print s.canJump([2, 3, 1, 1, 4])
print s.canJump([3, 2, 1, 0, 4])
print s.canJump(A)
print s.canJump(B)
end = timeit.default_timer()
print 'Total run time is', end - start
            
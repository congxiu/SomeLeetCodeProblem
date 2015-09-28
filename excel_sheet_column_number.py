# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:31:04 2015

@author: westlake3
"""

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        code_dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11,
        'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23,
        'X':24, 'Y':25, 'Z':26}
        p = 0
        n = len(s)
        
        for idx, char in enumerate(s):
            p = p + code_dic[char] * 26 ** (n - 1 - idx)
            
        return p
            
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        '''
        PAYPALISHIRING
        3 rows
        
        P   A
        A P L H
        Y   I
        
        PAHNAPLSIIGYIR
        
        1. Approach 1
        
        0 [PA]  -> [P,A,]
        1 [APL]
        2 [Y]
        
        Time O(n)
        Space O(n)
        
        n is the number of characters in string
        k is the numRows
        '''
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        delta = -1
        row = 0
        res = [[] for i in xrange(numRows)]
        
        #iterate through our string
        for c in s:
            res[row].append(c)
            if row == 0 or row == numRows - 1:
                delta *= -1
            row += delta
        
        #consolidate result
        for i in xrange(len(res)):
            res[i] = ''.join(res[i])
        return ''.join(res)
        
        
        '''
        2nd approach
        
        
        PAYPALISHIRING  numRows = 4
        row 0.  0 6 12 or    0 +6 +6
        row 1.  1 5 7 11 13  1 +4 +2 +4 +2
        row 2.  2 4 8 10.    2 +2+ 4 +2 +4
        row 3.  3 9          3 +6 +6
        
        P Y
        A P
        
        
        cycle = 2 * numRows - 2
        1 -> 1 special case
        2 -> 2
        3 -> 4
        4 -> 6
        
        Time O(n)
        Space O(1) or O(n)

        n is the number of characters in our input string
        Space is constant if we do not count our output (res variable)
        Otherwise it is O(n)
        '''
        if numRows == 1:
            return s
        
        cycle = 2 * numRows - 2
        res = []
        for i in xrange(numRows):
            for j in xrange(i, len(s), cycle):
                res.append(s[j])
                k = j + cycle - 2 * i
                if i != 0 and i != numRows - 1 and k < len(s):
                    res.append(s[k])
        
        return ''.join(res)
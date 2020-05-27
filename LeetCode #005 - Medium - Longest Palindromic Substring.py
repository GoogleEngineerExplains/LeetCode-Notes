class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        
        1. which approach to use?
            dp O(n^2)
            intuitive, expand around center O(n^2)
            manachers O(n)
        
        2. interviewing
           phone screen
           on-site
        
        3. our approach
            
              b a b a d
            o 1 3 3 1 1
            e 0 0 0 0 0
            
              c b b d
            o 1 1 1 1
            e 0 2 0 0 
           
          1. expand out from a middle letter
             stop when
             a. two letters are not the same
             b. edge of the string
             
             
             a b a
             l   r

        Time O(n^2)
        Space O(1) 
        '''
        
        #return length, left index, right index
        def longestAtIndex(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            return (r - l + 1, l, r)
        
        longest = 0
        left = 0
        right = -1
        for i in xrange(len(s)):
            for j in xrange(2):
                length, l, r = longestAtIndex(s, i, i + j)
                if length > longest:
                    longest = length
                    left = l
                    right = r
        return s[left:right + 1]
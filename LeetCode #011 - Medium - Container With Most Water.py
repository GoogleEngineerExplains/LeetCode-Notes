class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        '''
        Brute Force
        
        1. Check every set of two points
        
        [1,8,6,2,5,4,8,3,7]
        1 8
        1.  6
        1.    2
        
        8 6 
        8. 2.
        8.   5 
        ...
        
        Time O(n^2)
        Space O(1)
        
        10 -> 100
        100 -> 10000
        1000 -> 1000000

        '''
        best = 0
        for l in xrange(len(height)):
            for r in xrange(l + 1, len(height)):
                best = max(best, min(height[l], height[r]) * (r - l))
        return best
        
        
        '''
        Optimal Solution
        [1,8,6,2,5,4,8,3,7]
        
                              h  w
         1.              7 -> 1  8 -> 8
         1             3.  -> 1. 7 -> 7
         1           8     -> 1. 6 -> 6
         
         when checking the ends, the best area for the lower side is that area
         
           8              7 -> 7  7 -> 49
             6            7 -> 6
               2          7 -> 2
        
         algorithm:
         1. check l and r most heights
         2. calculate local area
         3. move in from the lower height
         
         Time  O(n)
         Space O(1)
        
         n is the length of your input array
        '''
        
        best = 0
        l = 0
        r = len(height) - 1
        while l < r:
            best = max(best, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best
            
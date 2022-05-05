class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        
        1. overview
            intervals = [[1,3],[2,6],[8,10],[15,18]]

            1 2 3 4 5 6 7 8 9 10 ...
            -----
              ---------   ------

            -----------   ------
        
        2. brute force
        
            [1,3],[2,6],[8,10],[15,18]
            time complexity O(n^2)
            
        3. optimal solution
        
            [1,3],[2,6],[3,4],[8,10],[15,18] (sorted)
        
        4. time and space complexity
            
            time
            O(nlogn) + O(n)  ===> O(nlogn)
            
            space
            O(1)
        
        '''
        
        #sorting defaults, sorting without mutating
        intervals.sort(key = lambda x: x[0]) #O(nlogn)
        #intervals = sorted(intervals)
        
        if not intervals:
            return []
        
        curr = intervals[0]
        res = []
        
        for pair in intervals: #O(n)
            if pair[0] <= curr[1]:
                curr[1] = max(curr[1], pair[1])
            else:
                res.append(curr)
                curr = pair
        res.append(curr)
        return res

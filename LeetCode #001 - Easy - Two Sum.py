class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Brute Force
        #Time O(n^2)
        #Space O(1)
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
        
        #Optimal Solution
        #Time O(n)
        #Space O(n)
        lib = {}
        for i,n in enumerate(nums):
            if n in lib:
                return [lib[n], i]
            lib[target - n] = i
        return []
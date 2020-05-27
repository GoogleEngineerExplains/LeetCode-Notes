class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        '''
        c a b c a b c b b
        l 0 0 0 1
        r 0 1 2 3 4 5 6 7
          1 2 3 3
        
        abcba
        
        calculate the length of substring ending at each index
        find the global maximum
        
        l =
        l of the previous substring OR
        1 + the index, the current character has last appeared
        
        Time O(n)
        Space O(k)

        n is the number of characters in the input string
        k is the number of unique possible characters (i.e. 26 is all lower case letters)
        '''
        longest = 0
        l = 0
        lib = {}
        
        for r,c in enumerate(s):
            if c in lib:
                l = max(l, lib[c] + 1)
            lib[c] = r
            longest = max(r - l + 1, longest)
        return longest
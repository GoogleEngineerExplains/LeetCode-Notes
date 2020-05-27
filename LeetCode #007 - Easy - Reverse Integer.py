class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        123 % 10 -> 3
        123 / 10 -> 12
        
        12 % 10 -> 2
        12 / 10 -> 1
        
        res
        3 * 10 -> 30
        30 + 2 -> 32
        32 * 10 -> 320
        320 + 1 -> 321
        
        -123 % 10 -> -3
        -12 % 10 -> -2
        -1 % 10 -> -1
        
        -321
        
        1. modulus of negative numbers (python 2)
        2. division of negative numbers (python 2)
        
        3. -2 ** 31 <= numbers <= 2 ** 31 - 1
        
        Time O(n) 
        Space O(n) *O(1)
        
        n is the number of digits in our input
    
        
        '''
        
        '''
        Correct Approach
        (No variables will overflow during calculation)
        '''
        def divide(number, divider):
            return int(number * 1.0 / divider)
        def mod(number, m):
            if number < 0:
                return number % -m
            return number % m
        
        MAX_INT = 2 ** 31 - 1 # 2147483647
        MIN_INT = -2 ** 31    #-2147483648
        
        res = 0
        while x:
            pop = mod(x, 10)
            x = divide(x, 10)
            if res > divide(MAX_INT, 10) or (res == divide(MAX_INT, 10) and pop > 7):
                return 0
            if res < divide(MIN_INT, 10) or (res == divide(MIN_INT, 10) and pop < -8):
                return 0
            res = res * 10 + pop
            
        return res
        
        
        '''
        Example of less correct approach
        '''
        MAX_INT = 2 ** 31 - 1 # 2147483647
        MIN_INT = -2 ** 31    #-2147483648
        # -2147483648
        
        negative = x < 0
        x = abs(x)
        res = 0
        
        while x:
            pop = x % 10
            x /= 10
            res = res * 10 + pop
        
        if negative:
            res = -res    
        if res > MAX_INT or res < MIN_INT:
            return 0
        return res
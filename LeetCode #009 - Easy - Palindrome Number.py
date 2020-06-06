class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''
        121
        121 -> true
        
        10
        01 -> false
        
        -121
        121- -> false
        
        1. create a backwards copy of the number
        2. if backwards copy is the same, return true
        
        c = 1234
        b = 0
        
        1234 % 10 -> 4
        1234 / 10 -> 123
        c -> 123
        b -> 0 * 10 + 4 -> 4
        
        123 % 10 -> 3
        123 / 10 -> 12
        c -> 12
        b -> 4 * 10 + 3 -> 43
        
        b -> 4321
        
        121
        121
        
        Test Cases:
        negative numbers -> false
        0 -> true
        
        1210
        b -> 0121
        
        Time O(n), O(log(k))
        Space O(1)
        
        n is the number of digits in x
        k is the size of the number  log 1000 -> 3, log 100 ->2
        

        '''    
        if x < 0:
            return False
        
        c = x
        b = 0
        
        while c:
            b = b * 10 + c % 10
            c /= 10
            
        return b == x
    
    
    
        '''
        Solution 2
        
        1234
        
        1221
        12
        12
        
        12321
        12
        12
        
        12
        43
        
        1. reverse half of the number, compare it with our original number
        
        even    x  b
        1221 -> 12 12 -> true
        1231 -> 12 13 -> false
        1321 -> 1  123 -> false
        
        odd      x.  b   b/10
        12321 -> 12  123  12    -> true
        12322 -> 12  223  22    -> false
        
        1230
        1210 -> 121
        b -> 12
        x -> 1
        
        Time O(n)
        Space O(1)
        n is the number of digits
        
        
        '''
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        b = 0
        while x > b:
            b = b * 10 + x % 10
            x /= 10
        
        return x == b or x == b / 10
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
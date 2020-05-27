class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        '''
        Valid
        '42' -> 42
        '   -42' -> -42
        '99999999999999' -> MAX_INT
        '1312zcxvzc' -> 1312
        
        Invalid
        'asdfas'  -> 0
        '  +asdkljfasd 9' -> 0
        '' -> 0
        
        1. whitespace
        2. a +/- symbol
        3. numbers
        4  between MAX_INT and MIN_INT constraints
        5. random characters
        
        Time O(n)
        Space O(1)
        
        n is the number of characters in your input string
        '''
        
        MAX_INT = 2 ** 31 - 1 # 2147483647
        MIN_INT = -2 ** 31    #-2147483648
        
        i = 0
        res = 0
        negative = 1
        
        #whitespace
        while i < len(str) and str[i] == ' ':
            i += 1
        
        #+/- symbol
        if i < len(str) and str[i] == '-':
            i += 1
            negative = -1
        elif i < len(str) and str[i] == '+':
            i += 1
        
        #check number 0-9
        checker = set('0123456789')
        while i < len(str) and str[i] in checker:
            if res > MAX_INT / 10 or (res == MAX_INT / 10 and int(str[i]) > 7):
                return MAX_INT if negative == 1 else MIN_INT
            res = res * 10  + int(str[i])
            i += 1
        
        #check the MAX / MIN int
        return res * negative
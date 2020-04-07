class Solution:
    def longestPalindrome(self, s: str) -> str:
        def revs(s):
            n = ''
            for i in s:
                n = i + n
            return n
        
        def check(s):
            if len(s) < 2:
                return True
            elif s[0] != s[-1]:
                return False
            else:
                return check(s[1:-1])
        
        def make(s,start,i,length):
            if start >= i and start + i < length and s[start - i] == s[start + i]:
                return make(s,start,i + 1, length)
            else:
                return s[start - i + 1:start + i]
        
        def make2(s,start,i,length):
            if start >= i and start + i + 1 < length and s[start - i] == s[start + i + 1]:
                return make2(s,start,i + 1, length)
            else:
                return s[start - i + 1:start + i + 1]
        length = len(s)
        maxi = ''
        ml = 0        
        for start in range(length):
            print('l', start)
            if start + 1 < length and s[start] == s[start + 1]:
                pal2 = make2(s,start,1,length)
                pal = make(s,start,1,length)
                # print(pal, pal2)
                if len(pal) > len(pal2) and len(pal) > ml:
                    maxi = pal
                    ml = len(maxi)
                elif len(pal2) > len(pal) and len(pal2) > ml:
                    maxi = pal2
                    ml = len(maxi)
            else:
                pal = make(s,start,1,length)
                # print(pal)
                if len(pal) > ml:
                    maxi = pal
                    ml = len(maxi)
        return maxi
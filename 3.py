class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = ''
        ml = 0
        for idx, ltr in enumerate(s):
            if ltr in maxi:
                maxi = maxi.split(ltr)[1] + ltr
            else:
                maxi = maxi + ltr
            ml = max(len(maxi),ml)
        return ml
        
        # maxi = 0
        # adict= dict()
        # restart = -1
        # for idx, ltr in enumerate(s):
        #     print(maxi)
        #     if adict.get(ltr) == None:
        #         print('T', ltr, idx)
        #         maxi = max(idx - restart, maxi)
        #     else:
        #         print('F', ltr, idx)
        #         maxi = max(min(idx - adict[ltr],idx - restart), maxi)
        #         restart = idx - 1
        #     adict[ltr] = idx
        #     print(maxi)
        # return maxi
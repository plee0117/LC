class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def check(subs, fulls):
            ls = len(subs)
            lf = len(fulls)
            if lf % ls == 0:
                upto = lf // ls
                ct = 0
                while ct < upto:
                    if subs != fulls[ls * ct: ls * (ct + 1)]:
                        return False
                    ct += 1
                return True
            else:
                return False
        
        l = len(s)//2 + 1
        pat = ''
        for idx, ltr in enumerate(s[:l]):
            if idx == 0:
                pat += ltr
            elif ltr == pat[0]:
                if check(pat, s):
                    return idx + 1
                else:
                    pat += ltr
            else:
                pat += ltr
        return False
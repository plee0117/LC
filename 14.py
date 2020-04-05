class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        leng = -1
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        cont = True
        while cont:
            leng += 1
            for i in strs:
                if len(i) <= leng:
                    cont = False
                    break
                elif strs[0][leng] != i[leng]:
                    cont = False
                    break
        return strs[0][:leng]
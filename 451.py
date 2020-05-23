class Solution:
    def frequencySort(self, s: str) -> str:
        chardict = {}
        for ltr in s:
            if ltr in chardict:
                chardict[ltr] += 1
            else:
                chardict[ltr] = 1
        ctdict = {}
        ctlist = []
        for key, val in chardict.items():
            if val in ctdict:
                ctdict[val].append(key)
            else:
                ctdict[val] = [key]
                ctlist.append(val)
        ctlist.sort(reverse = True)
        out = ''
        for i in ctlist:
            temp = [x * i for x in ctdict[i]]
            out += ''.join(temp)
        return out
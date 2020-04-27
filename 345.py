class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = 'aeiouAEIOU'
        s = list(s)
        vs = []
        for i, l in enumerate(s):
            if l in vowel:
                vs.append(i)
        print(vs)
        l = len(vs)
        if l == 0:
            return ''.join(s)
        for i in range(l//2):
            t = s[vs[i]]
            s[vs[i]] = s[vs[l - i - 1]]
            s[vs[l - i - 1]] = t
        return ''.join(s)
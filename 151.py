class Solution:
    def reverseWords(self, s: str) -> str:
        sl = [i for i in s.split(' ') if i != '']
        return ' '.join(sl[::-1])
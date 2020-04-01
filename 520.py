class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        c = word
        return word == c.lower() or word == c.upper() or word == c.capitalize()
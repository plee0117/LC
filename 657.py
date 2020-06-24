class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter
        if moves == '':
            return True
        c = Counter(moves)
        if c['L'] == c['R']:
            if c['U'] == c['D']:
                return True
        return False
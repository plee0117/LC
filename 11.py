class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        last = len(height) - 1
        lprev = -1
        rprev = -1
        for idx, h in enumerate(height):
            if h <= lprev:
                continue
            lprev = h
            jdx = last
            while jdx > idx:
                if height[jdx] >= rprev:
                    temp = (jdx - idx) * min(h, height[jdx])
                    if temp > m:
                        rprev = height[jdx]
                        last = jdx
                        m = temp
                jdx -= 1
        return m
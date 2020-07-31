class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old = image[sr][sc]
        if old == newColor:
            return image
        rlen = len(image)
        clen = len(image[0])
        def fill(row, col):
            nonlocal old, newColor, image
            if image[row][col] == old:
                image[row][col] = newColor
                if row > 0:
                    fill(row - 1, col)
                if row < rlen - 1:
                    fill(row + 1, col)
                if col > 0:
                    fill(row, col - 1)
                if col < clen - 1:
                    fill(row, col + 1)
        fill(sr, sc)
        return image
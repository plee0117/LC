class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def nextR(last,l):
            tem = []
            for idx in range(l+1):
                # print('i', idx)
                if idx > 0 and idx < l:
                    # print('adding', last[idx] + last[idx - 1])
                    tem.append(last[idx] + last[idx - 1])
                else:
                    # print('adding end', 1)
                    tem.append(1)
                # print(tem)
            return tem
        if numRows < 1:
            return []
        out = [[1]]
        for i in range(1, numRows):
            # print('h', out[i - 1], i)
            out.append(nextR(out[i - 1], i))
        return out
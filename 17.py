class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        ltrs = []
        for i in digits:
            if ltrs ==[]:
                tem = [n for n in l[int(i)-2]]
            else:
                tem = []
                for ltr in ltrs:
                    tem += [ltr + n for n in l[int(i)-2]]
                    print(tem)
            ltrs = tem
        return ltrs
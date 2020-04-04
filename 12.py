class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        divs = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        qs = []
        for idx, d in enumerate(divs):
            if num < d:
                qs.append(0)
            else:
                c = 0
                while num//d > 0:
                    num -= d
                    c += 1
                qs.append(c)
        roman = ''
        for idx, q in enumerate(qs):
            roman += symbols[idx]*q
        return roman                
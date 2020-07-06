class Solution:
    def checkValidString(self, s: str) -> bool:
        lp = []
        ast = []
        for idx,ltr in enumerate(s):
            if ltr == "*":
                ast.append(idx)
            elif ltr == "(":
                lp.append(idx)
            elif ltr == ")":
                if lp:
                    lp.pop()
                elif ast:
                    ast.pop()
                else:
                    return False
        if len(ast) < len(lp):
            return False
        else:
            while lp:
                if lp[-1] <= ast[-1]:
                    lp.pop()
                    ast.pop()
                else:
                    return False
            return True
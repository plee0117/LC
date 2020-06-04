class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = []
        upto = len(list2)
        isum = upto + len(list1)
        for idx, rest in enumerate(list1):
            if rest in list2[:upto]:
                upto = list2.index(rest)
                if isum > idx + upto:
                    common = [rest]
                    isum = idx + upto
                elif isum == idx + upto:
                    common.append(rest)
            elif common != []:
                upto -= 1
                if upto < 0:
                    break
        return common
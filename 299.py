class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sd = dict()
        gd = dict()
        bu = 0
        cow = 0
        for i, l in enumerate(secret):
            if l == guess[i]:
                bu += 1
            else:
                if l in sd:
                    sd[l] += 1
                else:
                    sd[l] = 1
                if guess[i] in gd:
                    gd[guess[i]] += 1
                else:
                    gd[guess[i]] = 1
        for i in sd.keys():
            if i in gd.keys():
                cow += min(sd[i],gd[i])
        return(str(bu)+'A'+str(cow)+'B')
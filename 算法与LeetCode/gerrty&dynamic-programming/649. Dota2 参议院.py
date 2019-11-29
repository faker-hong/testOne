class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        rq = list()
        dq = list()
        length = len(senate)

        for i in range(length):
            c = senate[i]
            if c == "R":
                rq.append(i)
            else:
                dq.append(i)

        while len(rq) > 0 and len(dq) > 0:
            r = rq[0]
            d = dq[0]

            if r > d:
                dq.append(d + length)
            else:
                rq.append(r + length)

            del rq[0]
            del dq[0]

        return "Dire" if len(rq) == 0 else "Radiant"

    # 参考
    def predictPartyVictory(self, senate):
        R, D = True, True
        senate = list(senate)
        person = 0
        while R and D:
            R, D = False, False
            for i in range(len(senate)):
                if senate[i] == 'R':
                    R = True
                    if person < 0:
                        senate[i] = '0'
                    person += 1
                elif senate[i] == 'D':
                    D = True
                    if person > 0:
                        senate[i] = '0'
                    person -= 1
        return "Radiant" if person > 0 else "Dire"


if __name__ == '__main__':
    S = Solution()
    result = S.predictPartyVictory('RDD')
    print(result)
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        n = len(price)

        def shopping(special, needs):
            if not sum(needs):  # 所需物品购买完
                return 0
            # 过滤掉大礼包中超过所需的
            special = list(filter(lambda x: all(x[i] <= needs[i] for i in range(n)), special))
            # 如果过滤后为空，就只能单价购买了
            if not special:
                return sum(needs[i] * price[i] for i in range(n))

            res = []
            for gift in special:
                res.append(gift[-1] + shopping(special, [needs[i] - gift[i] for i in range(n)]))
            return min(res)

        # 先过滤掉亏钱的大礼包
        special = list(filter(lambda x: x[-1] <= sum(x[i] * price[i] for i in range(n)), special))
        return shopping(special, needs)

'''
意图：在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。

如何解决：通过一个备忘录类专门存储对象状态。

应用实例： 1、后悔药。 2、打游戏时的存档。 3、Windows 里的 ctri + z。 4、IE 中的后退。 4、数据库的事务管理。

优点： 1、给用户提供了一种可以恢复状态的机制，可以使用户能够比较方便地回到某个历史的状态。 2、实现了信息的封装，使得用户不需要关心状态的保存细节。

缺点：消耗资源。如果类的成员变量过多，势必会占用比较大的资源，而且每一次保存都会消耗一定的内存。
'''
import random


class zombie:
    goldCoin = 0  # 金币数量
    sun = 0  # 阳光数量
    teWuBean = 0  # 特务豌豆射手数量
    goldenSunflower = 0  # 金属向日葵数量
    icyIceCactus = 0  # 寒冰仙人掌数量

    def disState(self):
        print('zombie game current status is as below:')
        print('goldCoin : {}'.format(self.goldCoin))
        print('sun : {}'.format(self.sun))
        print('teWuBean : {}'.format(self.teWuBean))
        print('goldenSunflower : {}'.format(self.goldenSunflower))
        print('icyIceCactus : {}'.format(self.icyIceCactus))

    def initState(self, goldCoin, sun, teWuBean, goldenSunflower, icyIceCactus):
        self.goldCoin = goldCoin
        self.sun = sun
        self.teWuBean = teWuBean
        self.goldenSunflower = goldenSunflower
        self.icyIceCactus = icyIceCactus

    def saveState(self):
        return memo(self.goldCoin, self.sun, self.teWuBean, self.goldenSunflower, self.icyIceCactus)

    def recoverState(self, memo):
        self.goldCoin = memo.goldCoin
        self.sun = memo.sun
        self.teWuBean = memo.teWuBean
        self.goldenSunflower = memo.goldenSunflower
        self.icyIceCactus = memo.icyIceCactus


class fightState(zombie):
    def fight(self):
        self.goldCoin = random.randint(1000, 100000)
        self.sun = random.randint(1000, 100000)
        self.teWuBean = random.randint(1, 10)
        self.goldenSunflower = random.randint(1, 10)
        self.icyIceCactus = random.randint(1, 10)


class memo():
    goldCoin = 0
    sun = 0
    teWuBean = 0
    goldenSunflower = 0
    icyIceCactus = 0

    def __init__(self, goldCoin, sun, teWuBean, goldenSunflower, icyIceCactus):
        self.goldCoin = goldCoin
        self.sun = sun
        self.teWuBean = teWuBean
        self.goldenSunflower = goldenSunflower
        self.icyIceCactus = icyIceCactus


if __name__ == "__main__":
    curState = fightState()
    curState.initState(10000, 9000, 10, 10, 10)
    print('现在植物大战僵尸游戏第8关已通关，马上开始打第9关了，目前游戏参数值如下:')
    curState.disState()
    state8 = curState.saveState()
    curState.fight()
    print('越是往后关卡越难，第9关打完了了，真是惨不忍睹，目前参数值如下:')
    curState.disState()
    print('完败呀，只能重打了，恢复到第8关通关的参数吧,恢复如下')
    curState.recoverState(state8)
    curState.disState()
    print('恢复完了，再开始第9关吧')
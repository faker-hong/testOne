import abc


class observer():
    def update(self):
        pass


class subject(metaclass=abc.ABCMeta):
    __observerList = []

    def attactObserver(self, obs):
        self.__observerList.append(obs)

    def removeObserver(self, obs):
        self.__observerList.remove(obs)

    def notifyObserver(self):
        for obs in self.__observerList:
            obs.update()


class Hero(subject):
    def move(self):
        print("向前走")
        super().notifyObserver()


class Monster(observer):
    def update(self):
        if self.isRange():
            print("受到怪物攻击")

    def isRange(self):
        return True


class Trap(observer):
    def update(self):
        if self.isRange():
            print("踩到陷阱")

    def isRange(self):
        return True


class Gift(observer):
    def update(self):
        if self.isRange():
            print("得到礼物")

    def isRange(self):
        return True


if __name__ == '__main__':
    hero = Hero()
    monster = Monster()
    gift = Gift()
    trap = Trap()

    hero.attactObserver(monster)
    hero.attactObserver(gift)
    hero.attactObserver(trap)

    hero.move()
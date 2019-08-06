def lemonadeChange(bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    five = 0
    ten = 0
    if bills[0] != 5:
        return False
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            ten += 1
            five -= 1
        elif bill == 20:
            if ten >= 1 and five >= 1:
                ten -= 1
                five -= 1
            elif five >=3:
                five -= 3
            else:
                return False
    return True


if __name__ == '__main__':
    print(lemonadeChange([5,5,10,10,20]))
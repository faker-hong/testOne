import numpy as np


def soft_max(L):
    result = []
    L_exp = np.exp(L)
    sum_L_exp = sum(L_exp)
    for i in L_exp:
        result.append(np.divide(i, sum_L_exp))
    return result


if __name__ == '__main__':
    L = [1, 2, 3, 4]
    result = soft_max(L)
    print(result)
    np.float_
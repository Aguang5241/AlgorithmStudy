import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def main():
    x = np.arange(0, 20, 0.1)
    # print(x)
    sns.set(style='ticks', font='Arial')
    fig = plt.figure()
    plt.plot(x, np.log2(x), label='O (log n)')
    plt.plot(x, x, label='O (n)')
    plt.plot(x, x * np.log2(x), label='O (nlog n)')
    plt.plot(x, x ** 2, label='O (n${^2}$)')
    x_ = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y_ = []
    for i in x_:
        y_.append(np.math.factorial(i))
    plt.plot(x_, y_, label='O (n!)')
    plt.ylim(-10, 200)
    plt.xlabel('n')
    plt.ylabel('O (f(n))')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()

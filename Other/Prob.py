import numpy as np
import matplotlib.pyplot as plt


def main():
    drawBoxPlot()


def randomDraw():
    x = np.random.randint(2, size=100)
    ones = np.count_nonzero(x)
    zeros = len(x) - ones
    print("ones: ", ones)
    print("zeros: ", zeros)
    fig, ax = plt.subplots()
    ax.hist(np.array((zeros, ones)), bins=range(2))
    plt.show()
    print(x[0])


def probDraw():
    x = np.arange(1, 6)
    y = np.array([12, 17, 15, 7, 20])
    # print(np.sort(y))
    # print(np.mean(y))
    fig, ax = plt.subplots(4, 1)
    ax[0].bar(x, y)
    print(y)
    ax[1].hist(y, bins=range(y.min(), y.max() + 1))
    ax[2].hist(np.sort(y), bins=range(y.min(), y.max() + 1))
    ax[3].hist(y, bins=x + np.mean(y))
    # ax[2].plot(x, y)
    plt.show()


def histogramExample():
    x = np.random.randint(2, size=100)
    y = np.arange(0, 101)
    print(x)
    print(y)
    fig, ax = plt.subplots()
    ax.hist(x, bins=y)
    plt.show()

def drawBoxPlot():
    list = [4,5,7,7,7,8,10,11,11,13,13,14] # [4,5,7,7,7,8,10,11,11,13,13,14]
    fig, ax = plt.subplots()
    ax.boxplot(list, vert=False, patch_artist=True,)
    plt.show()


if __name__ == "__main__":
    main()

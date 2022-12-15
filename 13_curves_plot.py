from matplotlib import pyplot as plt
from math import sin, cos, exp


def plotFunctions():

    x = range(0, 100)
    y_sin = [sin(i) for i in x]
    y_cos = [cos(i) for i in x]
    y_poly = [i**5 for i in x]
    y_exp = [exp(i) for i in x]

    plt.subplot(2, 2, 1)
    plt.plot(x, y_sin)
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.title("x vs sin(x)")

    plt.subplot(2, 2, 2)
    plt.plot(x, y_cos)
    plt.xlabel("x")
    plt.ylabel("cos(x)")
    plt.title("x vs cos(x)")

    plt.subplot(2, 2, 3)
    plt.plot(x, y_exp)
    plt.xlabel("x")
    plt.ylabel("exp(x)")
    plt.title("x vs exp(x)")

    plt.subplot(2, 2, 4)
    plt.plot(x, y_poly)
    plt.xlabel("x")
    plt.ylabel("x**5")
    plt.title("x vs x**5")

    plt.tight_layout()
    plt.show()


plotFunctions()

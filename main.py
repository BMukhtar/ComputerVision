import matplotlib.pyplot as plt
from pprint import pprint


def f(x):
    return 1.0 / (1.0 + 25.0 * (x ** 2))


x = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1]
y = [f(xn) for xn in x]


def lagr(x, y):
    a = []
    for i in range(len(y)):
        tmp = []
        prod = 1
        for j in range(len(y)):
            if j == i:
                continue
            prod *= x[i] - x[j]
        a.append(y[i] / prod)
    res = []
    for l in x:
        tmp = []
        for i in range(len(y)):
            prod = 1
            for j in range(len(y)):
                if j == i:
                    continue
                prod *= l - x[j]
            tmp.append(a[i] * prod)
        res.append(sum(tmp))
    return res


res = lagr(x, y)
plt.plot(x, res)
plt.show()
pprint(zip(res, [f(i) for i in x]))

from scipy import interpolate


def f(x, x_points, y_points):
    tck = interpolate.splrep(x_points, y_points)
    return interpolate.splev(x, tck)


print(f(1.25, x, y))

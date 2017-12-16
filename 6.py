from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data1x = np.array((
    10.0,
    8.0,
    13.0,
    9.0,
    11.0,
    14.0,
    6.0,
    4.0,
    12.0,
    7.0,
    5.0
))
data1y = np.array((
    8.04,
    6.95,
    7.58,
    8.81,
    8.33,
    9.96,
    7.24,
    4.26,
    10.84,
    4.82,
    5.68))

data2x = np.array((
    10.0,
    8.0,
    13.0,
    9.0,
    11.0,
    14.0,
    6.0,
    4.0,
    12.0,
    7.0,
    5.0
))

data2y = np.array((
    9.14,
    8.14,
    8.74,
    8.77,
    9.26,
    8.10,
    6.13,
    3.10,
    9.13,
    7.26,
    4.74))
data3x = np.array((
    10.0,
    8.0,
    13.0,
    9.0,
    11.0,
    14.0,
    6.0,
    4.0,
    12.0,
    7.0,
    5.0,
))
data3y = np.array((
    7.46,
    6.77,
    12.74,
    7.11,
    7.81,
    8.84,
    6.08,
    5.39,
    8.15,
    6.42,
    5.73
))
data4x = np.array((
    8.0,
    8.0,
    8.0,
    8.0,
    8.0,
    8.0,
    8.0,
    19.0,
    8.0,
    8.0,
    8.0,
))
data4y = np.array((
    6.58,
    5.76,
    7.71,
    8.84,
    8.47,
    7.04,
    5.25,
    12.50,
    5.56,
    7.91,
    6.89
))


def calc(x, y, label, color, lw):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    plt.plot(x, y, 'o', label=label)
    plt.plot(x, intercept + slope * x, color, label=label, lw=lw)


calc(data1x, data1y, '1', 'r', 2.5)
calc(data2x, data2y, '2', 'g', 2)
calc(data3x, data3y, '3', 'b', 1)
calc(data4x, data4y, '4', 'c', .5)

print('mean x : ', end='')
print(np.mean(data1x + data2x + data3x + data4x))
print('mean y : ', end='')
print(np.mean(data1y + data2y + data3y + data4y))

print('std deviation x : ', end='')
print(np.std(data1x + data2x + data3x + data4x))
print('std deviation y : ', end='')
print(np.std(data1y + data2y + data3y + data4y))

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

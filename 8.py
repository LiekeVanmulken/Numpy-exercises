import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import json
import math
import pprint

heavy_smokers = [18, 16, 18, 24, 23, 22, 22, 23, 26, 29, 32, 34, 34, 36, 36, 43, 42, 49, 46, 46, 57]
heavy_smokers.sort()

min = np.min(heavy_smokers)
max = np.max(heavy_smokers)
mode = stats.mode(heavy_smokers, axis=None).mode[0]
median = np.median(heavy_smokers)
mean = np.mean(heavy_smokers)
print("Median             : {}".format(median))
print("Mean               : {}".format(mean))
print("Mode               : {}".format(mode))

q75, q25 = np.percentile(heavy_smokers, [75, 25])
print("Lower quartile     : {}".format(q25))
print("Higher quartile    : {}".format(q75))

sRange = np.subtract(max, min)
iqr = q75 - q25
print("Range              : {}".format(sRange))
print("Interquartile range: {}".format(iqr))

lineGraphY = []
for i in range(0, len(heavy_smokers)):
    lineGraphY.append((i+1 / len(heavy_smokers)) * 5)

def graph():
    plt.plot(heavy_smokers, lineGraphY)
    plt.title("Time after smokers fell off treadmill in seconds against percentile")
    plt.ylabel("Percentage dropped out")
    plt.xlabel("Amount of seconds on treadmill")


def boxPlot():
    plt.boxplot(heavy_smokers)
    plt.ylabel("Time in seconds on the treadmill")
    plt.title("Heavy smokers running on the treadmill, fastest setting")


graph()
plt.savefig("graph8.png")
plt.show()

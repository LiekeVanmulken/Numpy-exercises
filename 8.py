import numpy as np
import scipy
import matplotlib.pyplot as plt
import json
import math

heavy_smokers = [18, 16, 18, 24, 23, 22, 22, 23, 26, 29, 32, 34, 34, 36, 36, 43, 42, 49, 46, 46, 57]

min = np.min(heavy_smokers)
max = np.max(heavy_smokers)
median = np.median(heavy_smokers)
mean = np.mean(heavy_smokers)
print("Median             : {}".format(median))
print("Mean               : {}".format(mean))

q75, q25 = np.percentile(heavy_smokers, [75, 25])
print("Lower quartile     : {}".format(q25))
print("Higher quartile    : {}".format(q75))

range = np.subtract(max, min)
iqr = q75 - q25
print("Range              : {}".format(range))
print("Interquartile range: {}".format(iqr))

plt.boxplot(heavy_smokers)
plt.ylabel("Time in seconds on the treadmill")
plt.title("Heavy smokers running on the treadmill, fastest setting")
plt.savefig("boxplot 8.png")
plt.show()

import numpy as np
import scipy
import matplotlib.pyplot as plt
import json
import math
from pprint import pprint

data = json.load(open('7.json'))
pprint(data)

state = []
bachelordegrees = []
incomes = []
for entry in data['data']:
    print(entry[0])
    state.append(entry[0])
    bachelordegrees.append(entry[1])
    incomes.append(entry[2])

mean_income = np.mean(incomes)
mean_degree = np.mean(bachelordegrees)
print('Median income: {}'.format(mean_income))
print('Median degrees: {}'.format(mean_degree))

std_income = np.std(incomes)
std_degrees = np.std(bachelordegrees)
print('Standard diviation income: {}'.format(std_income))
print('Standard diviation degrees: {}'.format(std_degrees))

x = incomes
y = bachelordegrees

plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.scatter(incomes, bachelordegrees)

plt.rcParams.update({'font.size': 6})
for i, txt in enumerate(state):
    plt.annotate(s=txt, xy=(x[i], y[i]))

plt.xlabel('Income')
plt.ylabel('Degree percentage')
plt.title('Correlation between income and degree')
plt.savefig("correlation 7.png")
plt.show()

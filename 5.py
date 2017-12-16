import matplotlib.pyplot as plt
import numpy as np


data = [140, 145, 160, 190, 155, 165, 150, 190,
     195, 138, 160, 155, 153, 145, 170, 175,
     175, 170, 180, 135, 170, 157, 130, 185,
     190, 155, 215, 150, 145, 155, 155, 150,
     155, 150, 180, 160, 135, 160, 130, 155,
     150, 148, 155, 150, 140, 180, 190, 145,
     150, 164, 140, 142, 136, 123, 155, 140,
     120, 130, 138, 121, 125, 116, 145, 150,
     112, 125, 130, 120, 130, 131, 120, 118,
     125, 135, 125, 118, 122, 115, 102, 115,
     150, 110, 116, 108, 95, 125, 133, 110,
     150, 108, 116, 140, 199, 148, 150, 112]


t = np.arange(0.0, 96, 1)

plt.hist(data, 30)

plt.xlabel('lbs')
plt.ylabel('count')
plt.title('Histogram of Exercise 5')
plt.grid(True)
plt.savefig("simpleplot 5.png")
plt.show()

print('mean : ')
print(np.mean(data))
print('standard deviation')
print(np.std(data))


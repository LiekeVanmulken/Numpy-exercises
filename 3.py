import numpy as np

result = np.ones((4, 4))
result[2][3] = 2
result[3][1] = 6
print(result)
print('\n\n')

result2 = np.diag(np.array([2, 3, 4, 5, 6]))
a = np.zeros((1, 5))
result2 = np.insert(result2, 0, [a], axis=0)
print(result2)

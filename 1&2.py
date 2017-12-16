import numpy as np

x = np.array([1, 2, 3, 4])
y = np.sum(x)
print(x)
print(y)

print('========')
# next thingy
a = np.array([0, 1, 2, 3])
print(a, a.ndim, a.shape, len(a), a.dtype)

a = np.array([0, 1, 2], dtype=float)
print(a)

print('========')
print(np.arange(10))
print('========')
print(np.arange(1, 9, 2))
print('========')
print(np.linspace(0, 1, 6))
print('========')
print('========')
print(np.ones((3, 3)))
print('========')
print(np.zeros((2, 2)))
print('========')
print(np.eye(3))
print('========')
print(np.diag(np.array([1, 2, 3, 4])))
print('========')
print(np.random.rand(4))
print('========')
print('========')



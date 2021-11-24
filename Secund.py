import numpy as np
from scipy import linalg
import time

dim = int(np.loadtxt('Second/2.txt', max_rows=1))
a = np.loadtxt('Second/2.txt', skiprows=1, max_rows=dim)
b = np.loadtxt('Second/2.txt', skiprows=dim + 1)

# Я сначала решил через numpy, а потом вспомнил, что лаба по scipy, и решил сравнить.
# Касательно эпизода можно сразу переходить к с.24

# tic = time.perf_counter()
# for i in range(1000):
#     np.linalg.solve(a, b)
# toc = time.perf_counter()
# print(f"Numpy {toc - tic:0.4f} секунд")
#
# tic = time.perf_counter()
# for i in range(1000):
#     linalg.inv(a).dot(b)
# toc = time.perf_counter()
# print(f"Scipy {toc - tic:0.4f} секунд")

ans = np.around(linalg.inv(a).dot(b), decimals=5)
# Solution
print(ans)
# Check
print(a @ ans - b)

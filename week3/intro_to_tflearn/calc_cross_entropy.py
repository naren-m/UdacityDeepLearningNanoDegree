import numpy as np

y = [0, 0, 0, 1, 0]

y_cap = [0.27, 0.11, 0.33, 0.10, 0.19]

cross_entropy = 0

for i in range(len(y)):
    cross_entropy += y[i] * np.log(y_cap[i])

cross_entropy *= -1
print("cross_entropy", cross_entropy)

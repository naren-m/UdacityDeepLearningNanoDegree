import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read data

df = pd.read_fwf('brain_body.txt')
x = df[['Brain']]
y = df[['Body']]

body_reg = linear_model.LinearRegression()
body_reg.fit(x, y)

plt.scatter(x, y)
plt.plot(x, body_reg.predict(x))
plt.show()

from sklearn.linear_model import LinearRegression
import pandas as pd
# import matplotlib.pyplot as plt



bmi_life_model = LinearRegression()

bmi_life_data = pd.read_csv('bmi_and_life_expectancy.csv')
print bmi_life_data.head()

x = bmi_life_data[['BMI']]
y = bmi_life_data[['Life expectancy']]

bmi_life_model.fit(x, y)

# plt.scatter(x, y)
# plt.plot(x, bmi_life_model.predict(x))
# plt.show()


laos_life_exp = bmi_life_model.predict(21.07931)
print laos_life_exp
import pandas as pd

df02 = pd.read_csv('dz.csv')

# Средняя зарплата по городу
mean_salary = df02.groupby('City')['Salary'].mean()
print(mean_salary)
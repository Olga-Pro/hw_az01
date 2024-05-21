import pandas as pd
df01 = pd.read_csv('Stocks_data.csv')

# Вывести первые 5 строк датафрейма
print(df01.head())

# Информация о датафрейме
print(df01.info())

# Статистическое описание датафрейма
print(df01.describe())
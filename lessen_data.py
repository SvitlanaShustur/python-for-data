import pandas as pd

months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = {
    'revenue': [100, 200, 300, 400],
    'items_sold': [23, 43, 54, 65],
    'new_clients': [10, 20, 30, 40]
}

df = pd.DataFrame(data=sales, index=months)
# print(df)

# vector = [1, 2, 3, 4] #cтворює список
# print(vector * 2)

# series = pd.Series([1, 2, 3, 4]) # створює серію pandas
# print(series * 2)

# series_str = pd.Series(['a', 'b', 'c']) # створює серію pandas зі строками
# print(series_str[0]) # виводить перший елемент серії
# print(series_str + 'd') # додає 'd' до кожного елемента серії


# months = ['Jan', 'Feb', 'Mar', 'Apr']
# sales = [100, 200, 300, 400]
# data = pd.Series(data=sales, index=months) # створює серію pandas з індексами
# print(data)
# print(data['Feb']) # виводить елемент серії з індексом 'Feb'

# print(df.head(2)) # виводить з початку рядка
# print(df.tail(1)) # виводить з кінця рядка
# print(df.revenue) # виводить стовпець revenue або
# print(df['revenue']) # виводить стовпець revenue

# print(df.info()) # виводить інформацію про датафрейм
# print(df.shape) # виводить розмір датафрейму    
# print(df.columns) # виводить назви стовпців
# print(df.describe()) # виводить статистичну інформацію про числові стовпці
# print(df.dtypes) # виводить типи даних стовпців

df.revenue = ["100a", "200", "300", "400"] # змінює тип даних стовпця revenue на строковий
# print(df)
# print(df.revenue.dtypes)
df.revenue = pd.to_numeric(df.revenue, errors="coerce") #  перетворює стовпець revenue на числовий тип даних
# print(df)
# print(df.revenue.describe())
# print(df.revenue.dtypes) # виводить тип даних стовпця revenue


# print(df.loc["Feb"]) # виводить рядок з індексом 'Feb'
# print(df.loc[["Feb", "Mar"]])  #виводить рядки з індексами 'Feb' та 'Mar' звертати увагу на подвійні дужки
# print(df.loc[["Feb", "Apr"]])  #виводить рядки з індексами 'Feb' та 'Apr' звертати увагу на подвійні дужки


movies_df = pd.read_csv("data/movies_metadata.csv") # завантажує датафрейм з csv файлу 
# print(movies_df.to_string()) # виводить увесь датафрейм
pd.options.display.max_rows = 10 # встановлює максимальну кількість рядків для відображення
print(pd.options.display.max_rows) # виводить максимальну кількість рядків для відображення